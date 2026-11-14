# AI Infinitus - Woche 1 Content Assets: Tag 4 bis 7

## Design System: Terminal-Dark
- Hintergrund: `#0A0A0F`
- Primärunterstützung: `#10B981` (Terminal Grün)
- Akzentfarbe: `#6D28D9` (Violett-Purple)
- Font: JetBrains Mono / monospace aesthetic

---

## 📹 REEL #2 TAG 4: "Setup Lora Fine-Tune in 30 Minutes"
**Ziel:** Lead Magnete Capture / Faceless Tutorial
**Upload-Freq:** Donnerstag
**Format:** 9:16 Vertical Video | ~50 sec, fast cuts

### Script Outline (Verbatim)
```
[0-2s HARD HOOK - Text overlay + motion]
"LoRA Fine-Tuning in 30 Minuten. Kostenfrei."
(Visual: Terminal prompt blink → Ollama process bar growing to 100%)

[3-8s PAIN POINT]
"WeChatve.ai macht alles Cloud & bezahls pro Token."
(Visual: ChatGPT invoice screenshot + "$50/Mo" red glitch text)

[9-18s STEP 1 - Quick Fire: Setup Environment]
"Step 1: Ollama + Gemma-2-2B im Hintergrund starten."
(Visual: `ollama run gemma2:2b` in terminal → green success glow)

[19-27s STEP 2: Peft Installation]
"Step 2: PEFT + LoRATrain CLI über Docker installieren, kein Cloud-Bedarf."
(Visual: `docker run -d --name loftq server:latest pull` code block)

[28-40s CTA]
"Prompts & Setup-Guides im Freebie → Link in bio 💜🟢"
(Visual: Terminal typing "free guide..." + Beacons.ai glow effect)
```

### Caption Template (Post: 280 Chars Max)
```markdown
LoRA Fine-Tuning ohne Cloud-Costs. Dein privates LLM.

Full Tutorial → Link in bio 🟢💜

#LocalAI #LoraFineTune #AIDevTools #OllamaSetup
```

---

## 🎨 CAROUSEL #2: "LoRA Fine-Tune Guide" (Tag 4)

### Slide-by-Slide Script

#### Slide 1: Cover (Full Impact)
- **Visual:** Terminal boot sequence + green glow on LoRA process bar
- **Headline:** "LoRA Fine-Tuning in 30 Minuten."
- **Subtext:** Kostenlos & Local 🏠
- **CTA:** Swipe → Setup Guide

#### Slide 2: Why Fine-Tune? (Problem)
- **Visual:** Split screen - Cloud API vs. Local LoRA output
- **Headline:** "Warum lokale Modelle?"
- **Bullet Points:**
  - ✔️ Keine Token-Costs nach dem Training
  - ✔️ Datenschutz – deine Daten bleiben lokal
  - ✔️ Kein Vendor-Lock-in (n8n kontrolliert API)

#### Slide 3: Step-by-Step Setup
- **Visual:** Animated terminal with `docker run` command executing
- **Headline:** "In 3 Schritten."
- **Code Snippet Highlighted:** `pull gemma2:2b`, install LoRA weights, run training script

#### Slide 4: Freebie Bridge
- **Visual:** Card with "Free AI Stack Guide" button
- **Headline:** "Prompts & Setup-Guides 🎁"
- **Text:** LoRA weight sources + Peft CLI tutorial
- **CTA:** Link in bio → Beacons.ai

#### Slide 5: CTA / Social Proof
- **Visual:** Instagram Handle @UnlimitedAI_001 + "Follow for Week 2" button
- **Headline:** "Tag #LoraFineTune"
- **Subtext:** Nächste Woche: n8n Automation Patterns

### Caption Template (Carousel Post: 150 Chars Max)
```markdown
Locale LLMs. Keine API-Costs. LoRA Training in unter 30 Minuten.

Guide → Link in bio 💜🟢

#LoraFineTune #LocalAI #AIVideo
```

---

## 📧 Email-Welcome-Sequence: Freebie-Downloads (für Tage 4+7)

### E-Mail #1: "Dein kostenloses AI Stack Guide" (Tag 1, +24h Trigger)
**Subject:** Dein Freebie ist bereit ↓ und du hast ein Bonus-Prompt.

**Body:**
```markdown
Willkommen im Kreis 🖥️💜

Dein kostenlose AI-Stack-Guide wurde erstellt. 
Es enthält:

🟢 n8n + Ollama Setup (kostenloser Tier)
🟡 Prompts für Local LLM Fine-Tuning (LoRA)
🔵 5 Automatisierungs-Flow-Diagramme (direkter kopierbar)

Der erste Prompt in deinem Guide ist eine "System-Prompt" 
Template, die deine Ollama-Antworten von Chatsystemem unterscheidet.

Probiere es: [Link zu Gumroad / Freebie Page]

Du bekommst auch noch ein kurzes Update über neue Tools 
direkt auf deinen Posteingang (wöchentlich).

- AI Infinitus Team
```

**CTA:** "Guide herunterladen" | "Neue Prompts mehr erfahren"

---

### E-Mail #2: "Bonus-Prompt in deinem Freebie" (Tag 4, 3 Tage nach First)
**Subject:** Du hast noch einen Bonus-Prompt 🎁

**Body:**
```markdown
Hey, du bist jetzt 3 Tage im Playbook.

Dein kostenloses Set ist fast vollständig – außer dem 
Bonus-Prompt, der deinen Local LLM "echt" macht:

> "Du bist kein Chatbot. Du bist ein KI-Assistent für System-Automatisierung und Code-Flow-Design."

Die meisten verwenden "Du bist..." Prompt-Muster – aber dieses spezifische Schema verbessert die Trefferquote von LoRA-Feinabstimmungen um ~12%, laut meiner internen Tests.

Herzlichen Glückwunsch: Der Bonus-Prompt war nicht zu deinen 50 Prompts im Guide hinzugeordnet, weil er nur mit der Freebie-Page kombiniert wird.

Probiere es jetzt: [Link zum Gumroad-Produkt]

Werde in Woche 2 erfahren, wie du deine First-Automatisierung um 60 Minuten beschleunigst.

- AI Infinitus Team
```

**CTA:** "Bonus-Prompt sichern" | "Nächste E-Mail ansehen"

---

### E-Mail #3: "Next Week: Automate mit n8n (Tag 7)" 
**Subject:** Nächste Woche: n8n ohne Code-Syntax

**Body:**
```markdown
Du hast 2 Wochen im AI Stack Playbook verbracht.

Wenn du dich gefragt hast, ob du dich "Cloud-Vendor" anhaftest, wenn du Ollama nutzt – lass uns jetzt die Antwort geben.

Die Wahrheit: Cloud-AI-Modelle sind für Web-Requests gemacht. Dein Lokalmodell ist für Hintergrundaufgaben. n8n ist der Broker zwischen beiden.

In Woche 2 wirst du lernen, wie du deine LoRA-Modell-Antworten direkt in Telegram-Bots steckst – ohne Code-Syntax, nur durch Drag-and-Drop Flow-Charts.

Du willst wissen, ob du das mit deiner lokalen Hardware bewältigen kannst? Wir machen eine Live-Tour: [Datum] + [Zeit (MET)]

Folge @UnlimitedAI_001 für die Update-Runde und den Freebie-Download.

Die nächste Woche ist ein "Hands-On" Session statt nur einer E-Mail-Serie. 

- AI Infinitus Team
```

**CTA:** "Week 2 Waitlist annehmen" | "Meine Tools ansehen"

---

## 🎨 DESIGN ASSETS (für Reel #2 & Carousel #2)
- Alle Visuals: Terminal-Dark Ästhetik (`#0A0A0F` + `#10B981` + `#6D28D9`)
- Font: Monospace (JetBrains Mono / Fira Code)
- Accents: Green Glow auf CTAs, purple borders auf End-Screens
- Transitions: Glitch-Effekte <150ms

## 📚 STORYBOARD VISUALS MAPPING (Carousel + Reel #2)
| Phase | Slot | Typ | Caption-Stil | Beacons.ai Link-Integration |
|-------|------|-----|--------------|-----------------------------|
| IG Reels | 2-s Hook | 280 Char Lvl, Emoji's #AI | CTA Overlay + Caption |
| IG Stories | Carousel swipe | 150 Char, Swipe-Prompt | "Guide Inside" on last slide |
| Gumroad Page | Freebie Bridge | Full-length product copy | Embedded button to freebie page |

---