graph TD
    Vault[Obsidian Vault .md Dateien] -->|1. Hermes File-Reader Tool| Hermes[Hermes Agent]
    Hermes -->|2. Extrahiert Skript & Visuals| PythonScript[Python Local Engine]
    PythonScript -->|3. Prompt per API| LTX[LTX 2.5 Model API]
    PythonScript -->|4. Text & Branding Overlay| FFmpeg[FFmpeg Local Renderer]
    FFmpeg -->|5. Fertiges Video + Metadata| n8n[n8n Local Webhook]
    n8n -->|6. Auto-Publish| Socials[YouTube & Instagram]