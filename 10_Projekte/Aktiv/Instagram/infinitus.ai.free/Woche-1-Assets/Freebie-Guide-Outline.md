# Full Guide: Mein Free AI Stack Guide (Lead Magnete)
## "Mein Free AI Stack" — 30-Tage Freebie v1 | infinitus.ai.free

**Veröffentlicht:** Woche 1 Tag 1  
**Produkt-Format:** PDF / Notion Template / Obsidian Bundle  
**Preis:** $0 (Freebie, CTA: "Upgrade zum Prompt Pack $7")  
**Email-Capture:** Beacons.ai Link-in-Bio → Google Form / EmailJS

---

## 🎯 VALUE PROPOSITION
```bash
┌─────────────────────────────────────────────────────┐
│  WHAT: Full Local AI Stack (Ollama + n8n + Prompts) │
│  WHO: Developers, Builders, AI Curious Non-Techies  │
│  WHEN: Instant Download | Lifetime Access           │
│  WHY: $0 Mondschein LLMs, Full Automation Free Tier│
└─────────────────────────────────────────────────────┘
```

**USP:** "Your Private Cloud. Zero API Keys. 100% Local Control."  
**Callout:** "$49/Mo per chat. Wir: $0 Mondschein + dein Strom."

---

## 📦 TABLE OF CONTENTS

### FREEBIE MODULE 1: AI SETUP (Werte-Stack)
| Modul | Content | Zeit | Format |
|-------|---------|------|--------|
| Step 1 | Ollama Install & Config | 3 min | Video + Checkliste |
| Step 2 | Model Download Guide (Llama/Mistral/Gemma) | 5 min | Screenshot Steps |
| Step 3 | Prompt Libraries für 7 Use Cases | 15 min | Copy-Paste Prompts |
| Bonus | n8n Webhook Test | 10 min | Terminal Commands + JSON Schema |

### FREEBIE MODULE 2: PRIORITY CHECKLISTS (Operative)
```markdown
## ✅ OLLAMA CHECKLIST
- [ ] Docker Desktop läuft (Windows)
- [ ] `curl https://ollama.com/install.sh | sh` exekutiert
- [ ] `whoami /all` → "user" im Output (Docker User) ✓
- [ ] `ollama list` zeigt >1 Model
- [ ] `ollama pull llama3.2` startet ohne Fehler

## ✅ N8N CHECKLIST
- [ ] n8n self-hosted läuft (/usr/bin/n8n)
- [ ] Webhook Test: cURL request → Status 200
- [ ] Localhost (http://localhost/5173) erreichbar
- [ ] Credentials Manager funktioniert → OAuth Token
```

### FREEBIE MODULE 3: PROMPT BANKS (Kopierbar)
#### Prompt Template: "Debug My n8n Workflow"
```markdown
🔧 Role: Your n8n Expert. Find the bug, suggest a fix.

Input: [paste your Workflow JSON or screenshot]
Output Format: 1) Problem summary + line #2) Fix code snippet (JSON/JS) + 3) Why this works

Example:
User: "My webhook keeps failing on POST"
AI Output:
1) Issue: Body parsing in Node.js not set → Use `{json:true}` header or n8n's native JSON node.
2) Code: Add `{json:true}` to n8n's Request Headers field OR use "JSON Parse" node before "Execute Workflow".
3) Why: n8n sends body as string by default. Set `json:true` for proper parsing.

[Add your workflow here]
```

#### Prompt Template: "Critique My Obsidian Notes Structure"
```markdown
🔍 Role: Senior AI Curator. Find gaps in this knowledge base.

Input: [paste Obsidian YAML frontmatter + notes content]
Output Format: 1) 3 Weaknesses (with fixes) + 2) New template suggestion + 3) Link to your prompt pack

Example:
User: "My Obsidian notes for AI are organized in one file."
AI Output:
[Your Critique with Actionable Fixes]
```

### FREEBIE MODULE 4: AUTOMATION BUILDER (End-to-End)
```yaml
# FULL WORKFLOW EXAMPLE: "Email → Ollama Chat → n8n Workflow"

1. TRIGGER: Google Calendar Event Created
   - Input: Email from team@company.com
   - Action: Gmail Send ("Meeting notes attached")

2. PROCESS: Ollama (Local LLM)
   - Input: Meeting attachment + "Summarize & extract action items"
   - Output: JSON with priorities, assignees, deadlines

3. PROCESS: n8n Webhook Handler
   - Input: JSON from Ollama
   - Action: Push to Airtable/Dropbox ("Action Item CSV")

4. OUTPUT: Email Notification (Team Members)
   - Recipients: team@company.com
   - Body: "Here are today's priorities..." (from Airtable field)
```

---

## 📥 DELIVERY ASSETS
### 1. PDF / ZIP CONTENT STRUCTURE
```
📦 Free-AI-Stack-Guide_v1.zip/
├── README.md              # Quick start, value prop
├── INSTALL_GUIDE.pdf     # Step-by-step Ollama + n8n
├── PROMPT_BANK.md        # 7 Copy-Paste Prompts
├── CHECKLISTS_CHECK.json # Interactive checklist (Airtable/Notion)
├── WORKFLOW_EXAMPLE.yml  # Full automation flow YAML
├── ERROR_LOGS_SOLUTIONS.pdf # Troubleshooting guide
└── THANKYOU_EMAIL.html   # Post-download engagement page
```

### 2. EMAIL AUTOMATION (EmailJS Template)
```markdown
Subject: Your Free AI Stack is here 🟢💜

Hi {name},

This is your personalized copy of "Free AI Stack Guide". 

To-Do:
1. Open guide.pdf & read Step 1 (Ollama Install)
2. Try `ollama pull llama3.2` → screenshot the terminal output
3. Share your first prompt result in IG DMs (tag @UnlimitedAI_001)

→ Upgrade to "Prompt Pack $7" if stuck? Link inside: {gumroad-url}

See you tomorrow on Instagram with the next tutorial. 💜

— The AI Infinitus Team
#LocalAI #OllamaGuide #FreeAIStack
```

### 3. THANKYOU PAGE (Beacons.ai / ConvertKit)
**Headline:** "Your Free AI Stack is ready! 🎁"  
**Subtext:** Download: [PDF Button] | Watch Video: [YouTube Embed]  
**Next Step:** "Join Waitlist for Prompt Pack $7" (Link in Bio)

---

## 🔗 CTA & TRACKING INTEGRATION
### Email Capture Link-in-Bio Map
```
BEACONS.AI → Google Form (Name/Email) | Send to: lead-capture@your-domain.com
↓
✅ Thank You Page (Free Guide + Upsell: "Prompt Pack $7")
→ Gumroad Checkout (Link)
```

### Gumroad Product Link Structure
```markdown
[Primary Product: Free AI Stack Guide v1] → Email capture | Thankyou page → Email automation

[A/B Test Option] → Prompt Pack ($7, 25+ Prompts + Setup Videos)
[Secondary Conversion] → n8n Workshop ($19, Full Workflow Tutorials)
```

### YouTube Video-to-Guide Bridge (Tag 3)
```bash
Video Description: "Free Guide to $0 Mondschein LLMs + Automation? 
→ Link in bio to download full PDF"

Pinned Comment: "💜 Download your Free AI Stack here → Beacons.ai ↓"

Caption #1: "Step-by-Step Setup guide inside! #AIAutomation #OllamaGuide"
Caption #2: "What's your favorite LLM? Comment below 🔥 (for IG engagement)"
```

---

## 📊 SUCCESS METRICS & ANALYTICS

| KPI | Target Week 1 | Tool Stack |
|-----|---------------|------------|
| Email Captures | >50 / Day | Google Form + EmailJS |
| PDF Downloads from Guide | >200 | Gumroad Analytics |
| Conversion Rate (Free → Paid) | >8% / $7 product | Gumroad + Beacons AI |
| IG Saves on Guide Post | >50 saves | IG Insights |
| CTR to Gumroad from Link-in-Bio | >30% | GA4 Pixel tracking |

### Data Pipeline Example (Tracking)
```yaml
1. IG Post → Link-in-Bio Beacons.ai
2. Form capture → lead-capture email address
3. Thank you page → redirect to PDF download + Gumroad upgrade button
4. Gumroad sale → email automation triggered via Mailchimp/ConvertKit
5. YouTube video → comment "Need guide!" → IG DM → guide PDF link

TRACKING: Google Analytics Pixel on landing page | Event tracking on "Download Guide" & "Add to Cart" buttons
```

---

## ⚙️ TECHNICAL DELIVERY NOTES

### 1. OLLAMA INSTALLATION (Example Step 1 Video)
**Script:**
- Open terminal → Run `curl https://ollama.com/install.sh | sh`
- Confirm installation: whoami /all shows correct user
- Pull model: ollama pull llama3.2
- Show terminal output → success checkmark

### 2. n8n LOCALHOST SETUP (Example Step 3 Video)
**Script:**
- Start n8n server: `/usr/bin/n8n`
- Send test webhook from Postman/VSCode REST Client
- Screenshot response: 200 OK → success

### 3. PROMPT BANK DELIVERY FORMAT (Markdown / PDF)
```markdown
## 🔧 Prompt Bank v1 (Copy-Paste Ready)

# Debug My n8n Workflow
🔧 **Role:** Your n8n Expert. Find the bug, suggest a fix.  
**Input:** [paste your Workflow JSON or screenshot]  
**Output Format:** 1) Problem summary + line #2) Fix code snippet (JSON/JS) + 3) Why this works  

[User fills here...]

---
# Critique My Obsidian Notes Structure
🔍 **Role:** Senior AI Curator. Find gaps in this knowledge base.  
**Input:** [paste Obsidian YAML frontmatter + notes content]  
**Output Format:** 1) 3 Weaknesses (with fixes) + 2) New template suggestion + 3) Link to your prompt pack  

[User fills here...]
```

### 4. UPSELL CROSS-SELL OPTIONS (Week 1 CTA Strategy)
```yaml
Free Guide → $7 Prompt Pack: "25+ Prompts for Obsidian/Ollama/n8n"
$7 Pack → $19 n8n Workshop: "Full Automation Workflow Tutorials + Video Guides"

Conversion Rate Target:
- Free → $7 upsell: 8%
- $7 → $19 cross-sell: 30%
```

---

## 📝 WEEKLY ACTION CHECKLIST (Freebie Delivery)
| Task | Owner | Due | Status |
|------|-------|-----|--------|
| Install Ollama + n8n on dev machine | Dev | D1 | ⬜ |
| Generate PDF / ZIP content structure | Ops | D2 | ⬜ |
| Set up Beacons.ai link-in-bio page | Ops | D3 | ⬜ |
| Launch IG post with "Free Guide" CTA | Content | D4 | ⬜ |
| Publish YouTube tutorial (guide bridge) | Content | D5 | ⬜ |
| Email automation + thank you page test | Marketing | D6 | ⬜ |
| Download analytics: PDFs, emails, Gumroad sales | Analytics | D7 | ⬜ |
