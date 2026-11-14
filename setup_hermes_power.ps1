[CmdletBinding()]
param(
    [string]$HermesHome = (Join-Path $env:USERPROFILE ".hermes"),
    [string]$ObsidianVault = "C:\Users\elvis\OneDrive\Documents\AI\Obsidian",
    [switch]$StartAcp,
    [switch]$StartGateway
)

$ErrorActionPreference = "Stop"

if ($PSVersionTable.PSVersion.Major -lt 7) {
    throw "Dieses Skript benoetigt PowerShell 7+. Im VS-Code-Terminal mit 'pwsh' starten."
}
if ($StartAcp -and $StartGateway) {
    throw "Bitte -StartAcp oder -StartGateway einzeln verwenden."
}

$HermesHome = [IO.Path]::GetFullPath($HermesHome)
$ObsidianVault = [IO.Path]::GetFullPath($ObsidianVault)
$repo = $PSScriptRoot
$sourceModel = "qwen3.5:4b"
$hermesModel = "qwen3.5:4b-hermes-64k"
$ollamaBaseUrl = "http://localhost:11434/v1"
$vaultMemory = Join-Path $ObsidianVault "HermesMemory"
$memoryPath = Join-Path $HermesHome "memories"
$configPath = Join-Path $HermesHome "config.yaml"

function Invoke-HermesConfigSet {
    param(
        [Parameter(Mandatory = $true)][string]$Key,
        [Parameter(Mandatory = $true)][string]$Value
    )

    & hermes config set $Key $Value
    if ($LASTEXITCODE -ne 0) {
        throw "Hermes konnte '$Key' nicht konfigurieren (Exit-Code $LASTEXITCODE)."
    }
}

function Set-MemoryJunction {
    if (-not (Test-Path -LiteralPath $ObsidianVault -PathType Container)) {
        throw "Der angegebene Obsidian-Vault wurde nicht gefunden: $ObsidianVault"
    }

    New-Item -ItemType Directory -Path $vaultMemory -Force | Out-Null
    New-Item -ItemType Directory -Path $HermesHome -Force | Out-Null

    if (Test-Path -LiteralPath $memoryPath) {
        $existing = Get-Item -LiteralPath $memoryPath -Force
        if ($existing.Attributes -band [IO.FileAttributes]::ReparsePoint) {
            $target = [string]$existing.Target
            if ($target -and [IO.Path]::GetFullPath($target).TrimEnd("\").Equals(
                [IO.Path]::GetFullPath($vaultMemory).TrimEnd("\"),
                [StringComparison]::OrdinalIgnoreCase
            )) {
                Write-Host "Hermes-Memory ist bereits mit dem Obsidian-Vault verknuepft."
                return
            }
            throw "Hermes-Memory ist bereits ein anderer Link. Bitte zuerst pruefen: $memoryPath"
        }

        foreach ($name in @("MEMORY.md", "USER.md")) {
            $oldFile = Join-Path $memoryPath $name
            $vaultFile = Join-Path $vaultMemory $name
            if ((Test-Path -LiteralPath $oldFile -PathType Leaf) -and
                -not (Test-Path -LiteralPath $vaultFile)) {
                Copy-Item -LiteralPath $oldFile -Destination $vaultFile
            }
        }

        $backupName = "memories.before-obsidian-" + (Get-Date -Format "yyyyMMdd-HHmmssfff")
        $backupPath = Join-Path $HermesHome $backupName
        Rename-Item -LiteralPath $memoryPath -NewName $backupName
        try {
            New-Item -ItemType Junction -Path $memoryPath -Target $vaultMemory | Out-Null
        }
        catch {
            if (-not (Test-Path -LiteralPath $memoryPath)) {
                Rename-Item -LiteralPath $backupPath -NewName "memories"
            }
            throw
        }
        Write-Host "Bisherige Memory-Dateien gesichert unter: $backupPath"
    }
    else {
        New-Item -ItemType Junction -Path $memoryPath -Target $vaultMemory | Out-Null
    }

    Write-Host "Hermes-Memory liegt jetzt im Obsidian-Vault: $vaultMemory"
}

try {
    Push-Location -LiteralPath $repo

    if (-not (Test-Path -LiteralPath $ObsidianVault -PathType Container)) {
        throw "Der angegebene Obsidian-Vault wurde nicht gefunden: $ObsidianVault"
    }

    $previousHermesHome = [Environment]::GetEnvironmentVariable("HERMES_HOME", "User")
    if (-not $previousHermesHome) { $previousHermesHome = $env:HERMES_HOME }
    if (-not $previousHermesHome -and $env:LOCALAPPDATA) {
        $previousHermesHome = Join-Path $env:LOCALAPPDATA "hermes"
    }
    if ($previousHermesHome) {
        $previousHermesHome = [IO.Path]::GetFullPath($previousHermesHome)
        $sameHome = $previousHermesHome.TrimEnd("\").Equals(
            $HermesHome.TrimEnd("\"),
            [StringComparison]::OrdinalIgnoreCase
        )
        if (-not $sameHome -and (Test-Path -LiteralPath (Join-Path $previousHermesHome "config.yaml"))) {
            throw "Eine bestehende Hermes-Konfiguration liegt unter '$previousHermesHome'. Um kein Profil zu wechseln oder Daten zu uebergehen, starte mit -HermesHome '$previousHermesHome' oder migriere das Profil bewusst."
        }
    }

    if (-not (Get-Command ollama -ErrorAction SilentlyContinue)) {
        throw "Ollama wurde nicht gefunden. Installiere Ollama oder fuege ollama.exe zum PATH hinzu."
    }

    try {
        Invoke-RestMethod -Uri "http://localhost:11434/api/tags" -TimeoutSec 5 | Out-Null
    }
    catch {
        throw "Ollama antwortet nicht unter http://localhost:11434. Starte Ollama und fuehre das Skript erneut aus."
    }

    & ollama show $sourceModel 2>$null | Out-Null
    if ($LASTEXITCODE -ne 0) {
        throw "Das Basismodell '$sourceModel' ist nicht lokal vorhanden. Zuerst 'ollama pull $sourceModel' ausfuehren."
    }

    $modelfile = Join-Path $repo "Modelfile"
    if (-not (Test-Path -LiteralPath $modelfile -PathType Leaf)) {
        throw "Modelfile fehlt im Repository: $modelfile"
    }

    Write-Host "Erstelle Ollama-Modell '$hermesModel' mit 64.000 Kontext-Tokens..."
    & ollama create $hermesModel -f $modelfile
    if ($LASTEXITCODE -ne 0) {
        throw "Ollama konnte '$hermesModel' nicht erstellen (Exit-Code $LASTEXITCODE)."
    }

    if (-not (Get-Command hermes -ErrorAction SilentlyContinue)) {
        if (-not (Test-Path -LiteralPath (Join-Path $repo "activate.ps1") -PathType Leaf)) {
            throw "Hermes ist nicht installiert und activate.ps1 fehlt im Repository."
        }
        . (Join-Path $repo "activate.ps1")
    }

    [Environment]::SetEnvironmentVariable("HERMES_HOME", $HermesHome, "User")
    $env:HERMES_HOME = $HermesHome
    New-Item -ItemType Directory -Path $HermesHome -Force | Out-Null

    if (-not (Get-Command hermes -ErrorAction SilentlyContinue)) {
        throw "Der Hermes-Befehl ist nach der Aktivierung nicht verfuegbar."
    }

    Set-MemoryJunction

    if (Test-Path -LiteralPath $configPath -PathType Leaf) {
        $backupPath = "$configPath.backup-$(Get-Date -Format 'yyyyMMdd-HHmmssfff')"
        Copy-Item -LiteralPath $configPath -Destination $backupPath
        Write-Host "Vorhandene Konfiguration gesichert unter: $backupPath"
    }

    Invoke-HermesConfigSet "model.provider" "ollama"
    Invoke-HermesConfigSet "model.default" $hermesModel
    Invoke-HermesConfigSet "model.base_url" $ollamaBaseUrl
    Invoke-HermesConfigSet "model.context_length" "64000"
    Invoke-HermesConfigSet "model.ollama_num_ctx" "64000"
    Invoke-HermesConfigSet "memory.memory_enabled" "true"
    Invoke-HermesConfigSet "memory.user_profile_enabled" "true"

    Write-Host ""
    Write-Host "Hermes Power-Setup abgeschlossen."
    Write-Host "Konfiguration: $configPath"
    Write-Host "Memory-Vault:  $vaultMemory"
    Write-Host "HERMES_HOME wurde fuer neue Prozesse auf '$HermesHome' gesetzt."
    Write-Host "Starte VS Code neu, damit neue Terminals die Benutzervariable HERMES_HOME erben."
    Write-Host "Hinweis: 64k Kontext erhoeht den RAM-/VRAM-Bedarf von Ollama."

    if ($StartAcp) {
        Write-Host "Starte Hermes ACP im Vordergrund (stdio)..."
        & hermes acp
        if ($LASTEXITCODE -ne 0) {
            throw "hermes acp wurde mit Exit-Code $LASTEXITCODE beendet."
        }
    }
    elseif ($StartGateway) {
        Write-Host "Starte Hermes Gateway im Vordergrund..."
        & hermes gateway run
        if ($LASTEXITCODE -ne 0) {
            throw "hermes gateway run wurde mit Exit-Code $LASTEXITCODE beendet."
        }
    }
}
finally {
    Pop-Location
}
