# Prompt Pack v2.0 – Struktur & Inhalt für die Erweiterung des digitalen Produkts auf Gumroad
## Tiered Pricing: $7 / $19 / $25 (Lifetime Access + Weekly Updates)

**Erstellt:** 2026-10-15 | **Version:** 1.0 | **Status:** Plan Phase  
**Produkt-Nr.:** GRRM9AI2P3 (v2.0 – In Entwicklung)  
**Kategorie:** AI Automation / n8n + Ollama Guide / Prompt Engineering  

---

## 🎯 WIE VOM $7 PROMPT-PACK ZUM $25 COMPLETE STACK

### Der Verkaufs-Verlauf:
```
Free Guide ($0)
  ↓ (Week 1: Setup → Workflow)
Prompt Pack v1.2 ($7, Week 2 launch)
  ↓ (Upsell: Video Tutorials + Workflows)
Complete AI Stack ($25 – Week 3 launch)
```

### Die Psychologie:
- **$7**: "Prompt Library" als Entry-Level (keine Videos, nur Text-Prompts)
- **$19**: "Video Pack" für Visual Learners (4 Workshop-Videos + Prompts)
- **$25**: Complete AI Stack (Videos + Workshops + GitHub API Integration + 6-Mon Updates)

---

## 📦 PROMPT_PACK_V2.0_STRUCTURE (ALL_TIERS_SHARED)

### MODULE 1: AI SETUP & CONFIGURATION ($0 Freebie / $7+)
```bash
Module 1: "Your Local LLM Stack" – Setup Guide für Ollama/n8n/Obsidian
------------------------------------------
✅ Step 1: Ollama Install & Config (Windows/Mac/Linux)
   - Terminal commands + `whoami /all` verification (Docker User check)
   - First-run success screenshot (green bar animation)

✅ Step 2: Model Download Guide (Llama / Mistral / Gemma)
   - RAM requirements (8GB recommended, 16GB for large models)
   - "First run" screenshots showing success (`ollama list`)

✅ Step 3: System Prompt Templates (7 Use Cases)
   - Debug n8n Workflow + JSON Output
   - Critique Obsidian Notes Structure + Fix Gaps
   - Summarize Email to Action Items
   - Create Structured JSON for Automation Ready
   - Extract Metadata from PDFs
   - Generate YAML Frontmatter
   - Convert Chat Logs to Knowledge Graph

📸 Assets: PDF Download + ZIP Archive (4 Modules)
```

### MODULE 2: CHECKLISTS & DIAGNOSTICS ($7–$25 Tiered)
```markdown
**Module 2: "Troubleshooting & Debugging" – Operational Playbook**

#### OLLAMA CHECKLIST (All Tiers)
- [ ] Docker Desktop running (Windows/Mac/Docker Engine)
- [ ] `curl https://ollama.com/install.sh | sh` executed successfully
- [ ] `whoami /all` → "user" in output (Docker User) ✓
- [ ] `ollama list` shows >1 Model installed
- [ ] `ollama pull llama3.2` starts without errors

#### N8N CHECKLIST (All Tiers: +Webhook Validation)
- [ ] n8n self-hosted running (/usr/bin/n8n on Linux, Docker for Windows/Mac)
- [ ] Webhook test: cURL request → Status 200 OK received
- [ ] Localhost accessible (http://localhost/5173 for n8n Dashboard UI)
- [ ] Credentials Manager functioning → OAuth Token retrieved

#### JSON OUTPUT CHECKLIST ($19+ Tier Only)
- [ ] Response parsed correctly in n8n HTTP Request node
- [ ] Body format matches expected schema (`json:true` header set)
- [ ] Error logged when invalid input provided

📸 Assets: 1-page PDF Checklists + Interactive Terminal Test
```

### MODULE 3: PROMPT LIBRARY ($0 Freebie / $7+)
```markdown
**Module 3: "Copy-Paste Prompts" – AI Assistant Templates**

#### Template 1: Debug My n8n Workflow (All Tiers)
🔧 **Role:** Dein n8n Senior Engineer. Finde den Fehler, schlage eine Korrektur vor.  
**Input:** [Füge deinen Workflow JSON oder Screenshot ein]  
**Output Format:**  
1) Problem summary + Zeile/Variable  
2) Code-Fix Snippet (mit JSON/JS + n8n Feld-Extraktion)  
3) Erklärung "Warum"

#### Template 2: Structured Output (JSON Schema) ($7+ Tier Only)
🔧 **Role:** Senior AI Engineer mit JSON-Schema-Expertenwissen. Finde Lücken im Ausgabeformat.  
**Input:** User Request + Output Constraints (`{"format": "json"}` als Header)  
**Output Format:** `{role, action, data}` – bereit für n8n HTTP Request Handler

#### Template 3: System-Customization ($19 Tier Only)
🔧 **Role:** Dein AI Engineer mit Prompt-Erweiterungsfähigkeiten. Erstelle Prompts anstatt nur zu antworten.  
**Input:** User Request + Custom Constraints (Temperature, Max Tokens)  
**Output Format:** [Verfeinertes Prompt] + `{{System: "Du bist ein..."}}`

#### Template 4: Email-to-Airtable Automation ($25 Tier Only)
🔧 **Role:** Senior AI-Engineer für Datenverarbeitung & Automatisierung  
**Input:** User Email / Meeting Notes attachment  
**Output Format:**  
1) Summary (mit Priorität, Zuweisung, Deadline) + CSV-Export  
2) Action Item Extraction JSON (JSON Schema mit `{"type":"array", "items": [{"priority": 1, "assignee": "user"}, {...}]}`)

📸 Assets: 8+ Copy-Paste Prompts + ZIP Archive  
```

---

## 🎞️ VIDEO PACK & WORKSHOP ($19 / $25 Tiered)

### Module 4: Video Walkthroughs (Exclusive to $19/$25 Tier)
```markdown
**Module 4: "AI Workflow Setup Walkthrough" – 4-Video Playlist (4 Min each)**

#### VIDEO 1: Ollama + n8n Installation & Config in 7 Minuten
- **Titel:** "Setup Your Private Cloud in <10 Mins"
- **Umschlagtext:** "$0 Mondschein, volle Kontrolle über deine Daten."
- **Inhalt:** Docker installieren → Modèles laden → Test API Request
- **Asset:** Video Guide (4 Min) + Terminal Screenshot Animation

#### VIDEO 2: Debugging Your AI Workflow in n8n (Real-Time)
- **Titel:** "Deine KI-Assistent für lokale Modelle bauen"
- **Umschlagtext:** "Fehler finden, ohne Python-Kenntnisse zu benötigen."
- **Inhalt:** HTTP Request Node → JSON Parsing → Debugging mit System Prompts
- **Asset:** Video Guide (4 Min) + n8n Workflow Export

#### VIDEO 3: Prompt Engineering Mastery (System-Patterns vs. Chat-Mode)
- **Titel:** "Warum dein Chatbot 'echt' wirkt"
- **Umschlagtext:** "Trainiere dein LLM mit dem Loopback-Prompt."
- **Inhalt:** System-Prompt Template + LoRA-FineTune Training Guide (Bonus-Content)
- **Asset:** Video Guide (4 Min)

#### VIDEO 4: Complete AI Stack (GitHub+Airtable Integration)
- **Titel:** "Deine Automatisierung aus lokalen Daten erstellen"
- **Umschlagtext:** "PDFs → Airtable → Telegram ohne Cloud-Aufrufe."
- **Inhalt:** API Key Management, Webhook Handler Setup, Email Automation Pattern
- **Asset:** Video Guide (4 Min)

📸 Assets: 4-Video Playlist + Weekly AI Newsletter Access ($19/$25 Tier)
```

---

## 🚀 GITHUB INTEGRATION + WORKSHOP UPSELLS

### Module 5: "AI Assistant Integration" – Exclusive to $25 Tier Only
```markdown
**Module 5: "Complete Automations Stack" – Live Workshop Access ($25+ Only)**

#### GitHub API & Airtable Integration (Lifetime Updates Included ✅)
- **GitHub + n8n Automation:** Workflow Export → Action Items → Issue Creation
- **Airtable Integration:** Meeting Notes Summary → Action Item CSV
- **Weekly Newsletter Access:** Lifetime Subscription (Free Bonus via Gumroad $7/$19/$25 Tiers)

#### Workshop Access: Week 3 Prompt Pack v2.0 ($25 Tier Only)
- **Workshop Content:** Live Demo + n8n Automation Patterns
- **Bonus:** Weekly Updates (6-Month Commitment)
- **Support:** Questions via IG DM / Email Support ($19/$25 Tiers only)

📸 Assets: Full Stack Automation Guide + GitHub API Integration Tutorial

---

## 💲 PRICING TIERS & DELIVERABLES

### Tier 1: $7 "Prompt Pack v1.2" (Entry-Level)
**Deliverables:**
- ☑️ Module 1: Setup Guide (PDF + ZIP)
- ☑️ Module 2: Checklists (1-page PDFs, all tiers)
- ☑️ Module 3: Prompt Library (8+ Copy-Paste Prompts, Text-Only)
- ☑️ Weekly AI Newsletter Access (Lifetime via Freebie Purchase)

**Upsell Path:** $7 → $19 (Video Tutorials + Workshops unlock)

---

### Tier 2: $19 "Prompt Pack + Video Pack" (Intermediate)
**Deliverables:**
- ✅ All $7 Tier deliverables
- ☑️ Module 4: Video Walkthroughs (4x 4-Min videos, Playlist access)
- ☑️ Weekly AI Newsletter Access (Lifetime via Purchase)
- ☑️ Support access via IG DM / Email ($19/$25 Tiers only)

**Upsell Path:** $19 → $25 (Complete Stack + GitHub Integration unlock)

---

### Tier 3: $25 "Complete AI Stack" (Premium/Lifetime)
**Deliverables:**
- ✅ All $19 Tier deliverables
- ☑️ Module 5: Complete Automations Stack (GitHub+Airtable Integration Tutorial)
- ☑️ Live Workshop Access (Week 3: Hands-On Session)
- ☑️ Weekly Updates for 6-Month Commitment ($25+ Tiers only)
- ☑️ Support with IG DM / Email Questions (Lifetime access to updates)

**Upsell Path:** No further upgrade (max tier). Optional annual subscription at $99.

---

## 🔗 GUMROAD TECHNICAL SETUP (Ops Note)

### Product Page URL Structure:
```markdown
Product 1: "Free AI Stack Guide v1"  
Price: Free | Link → Gumroad free product page  

Product 2: "$7 Prompt Pack v1.2 – Lifetime Access"  
Price: $7.00 USD | Auto-Delivery via Gumroad API  

Product 3: "$19 Prompt Pack + Video Pack – Lifetime Access"  
Price: $19.00 USD | Auto-Delivery via Gumroad API  

Product 4: "$25 Complete AI Stack – Lifetime Updates (6-Mo Commitment)"  
Price: $25.00 USD | Auto-Delivery via Gumroad API
```

### Tiered Upsell Options:
- **Free → $7:** "Prompt Pack v1.2" upsell on Free download page
- **$7 → $19:** "Add Video Tutorials" one-click upgrade option
- **$19 → $25:** "Complete Stack + 6-Month Updates" upsell

### GA4 + Pixel Tracking Events:
```json
{
  "metric_name": "gumroad_purchase",
  "parametric_event_name": null,
  "event_label": [
    "product_id_0", // Freebie guide
    "prompt_pack_v12_tier7", 
    "prompt_pack_video_pack_tier19", 
    "complete_ai_stack_tier25"
  ]
}

{
  "parametric_event": {
    "event_name": "gumroad_upsell",
    "parametric_event_name": [
      "upgrade_free_to_7",
      "upgrade_7_to_19",
      "upgrade_19_to_25"
    ],
    "parametric_event_label": "upsell_conversion"
  }
}
```

---

## 🛡️ TRUST & SECURITY (Cross-Tier Consistency)

### Privacy Promise:
- **Your Data stays local.** Ollama runs on your machine. No cloud API calls unless you enable them (opt-out).
- **No tracking, no cookies beyond standard Gumroad form**
- **Email address sent via Google Form / EmailJS (you control the list)**

### Refund Policy:
| Price Point | Guarantee Details |
|-------------|-------------------|
| $0 Free Guide | No refunds available (lifetime access already granted) |
| $7 Prompt Pack | 30-day satisfaction guarantee or full refund if setup fails |
| $19 Video Pack | Same 30-day guarantee plus IG DM / Email Support lifetime |
| $25 Complete Stack | Same + 6-Month Commitment Bonus (Weekly Updates) |

---

## 📈 KPIs & REVENUE PROJECTIONS

### Conversion Funnel:
```
Email Captures (Free Guide): 150–300 / Week
↓
Gumroad Conversion Rate: $7 Tiers → ~12% | $19 Tiers → ~4% | $25 Tiers → ~1.5%
↓
Weekly Revenue Projection (Weeks 4+ with Email Automation):
$7 Tier × 30 Subscribers = €21–€35/week
$19 Tier × 10 Subs = €190–€300/month
$25 Tier × 5 Subs = €125/mo

Combined weekly revenue goal: €40–€60/Week by Week 4 | €120+/Mo cumulative
```

### Gumroad Analytics to Track:
- `product_impression`: Product page view (Free Guide, $7 Upgrade)
- `add_to_cart`: User adds "Prompt Pack" or "n8n Workshop" to cart
- `purchase_completed`: Gumroad purchase event triggers email automation
- `upsell_conversion`: Success rates for upgrading tiers

---

## ⚙️ EMAIL CAPTURE SCRIPT (GUMROAD SUBMIT FORM COPY)

### Subject:  
```markdown
Dein kostenloses AI Stack Guide + 3 Bonus-Skripts für deinen First Workflow ↓🟢💜
```

### Email Body ($7 Tier Capture):
```markdown
Hey {name},

Willkommen im Woche-2 Playbook! Dein kostenloses AI-Stack-Guide wurde erstellt.

Zu deinem To-Do (3 Schritte):
1. Öffne guide.pdf & lies Schritt 1 (Ollama Install)
2. Versuche `ollama pull llama3.2` → mache einen Screenshot des Terminal-Ausgangs
3. Teile dein erstes Prompt-Ergebnis in IG DMs (tag @UnlimitedAI_001)

Upgrade-Pass ($7):  
Stuck auf Setup? Deine Prompt-Library + 5 Automation-Templates: 
→ https://gumroad.com/grrm9ai2p3

Probiere jetzt: $7 Lifetime Access + Weekly AI Newsletter
→ Prompt Library (Copy-Paste Ready)
→ Troubleshooting Scripts (JSON Checklists)
+ Video Workflows (Upgrade Option $19–$25)

— AI Infinitus Team (@UnlimitedAI_001)
```

### Call-to-Action Buttons:
**Primary Button:** "Prompt Pack v1.2 ($7 – Lifetime Access)" → Gumroad Product Page  
**Secondary Button:** "Next Tutorial Preview" → Beacons.ai Link-in-Bio  

---