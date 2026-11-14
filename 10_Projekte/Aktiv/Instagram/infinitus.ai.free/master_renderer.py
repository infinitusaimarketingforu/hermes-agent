import os
from string import Template
from html2image import Html2Image

VAULT_PATH = r"C:\Users\elvis\OneDrive\Documents\AI\Obsidian\Arbeit\10_Projekte\Aktiv\Instagram\infinitus.ai.free"
OUTPUT_DIR = os.path.join(VAULT_PATH, "IG_Post_Pakete", "Karussell_Docker_Setup")
os.makedirs(OUTPUT_DIR, exist_ok=True)

hti = Html2Image(output_path=OUTPUT_DIR)
hti.browser_window_size = (1080, 1080)

masterpiece_template = Template("""
<!DOCTYPE html>
<html>
<head>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800;900&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1080px; height: 1080px;
    background-color: #030305;
    background-image: 
      radial-gradient(circle at 50% 10%, rgba(124, 58, 237, 0.28) 0%, transparent 55%),
      radial-gradient(circle at 90% 90%, rgba(16, 185, 129, 0.18) 0%, transparent 45%),
      linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 40px 40px, 40px 40px;
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #F8FAFC; display: flex; flex-direction: column; justify-content: space-between; padding: 75px; position: relative; overflow: hidden;
  }
  .top-glow { position: absolute; top: 0; left: 0; right: 0; height: 6px; background: linear-gradient(90deg, #7C3AED, #3B82F6, #10B981); }
  .header { display: flex; justify-content: space-between; align-items: center; z-index: 2; }
  .badge { font-family: 'JetBrains Mono', monospace; font-size: 17px; font-weight: 700; color: #A78BFA; background: rgba(124, 58, 237, 0.15); padding: 8px 20px; border-radius: 30px; border: 1px solid rgba(124, 58, 237, 0.4); letter-spacing: 1.5px; text-transform: uppercase; }
  .counter { font-family: 'JetBrains Mono', monospace; font-size: 18px; color: #94A3B8; font-weight: 600; background: rgba(255, 255, 255, 0.04); padding: 6px 18px; border-radius: 20px; border: 1px solid rgba(255, 255, 255, 0.08); }
  .title-section { margin-top: 10px; margin-bottom: 20px; z-index: 2; }
  .main-title { font-size: 50px; font-weight: 900; line-height: 1.1; letter-spacing: -2px; color: #FFFFFF; }
  .card { background: rgba(10, 10, 16, 0.85); border: 1px solid rgba(255, 255, 255, 0.12); border-radius: 32px; padding: 40px 45px; backdrop-filter: blur(30px); display: flex; flex-direction: column; gap: 20px; flex-grow: 1; justify-content: center; margin-bottom: 20px; z-index: 2; }
  .window-controls { display: flex; align-items: center; gap: 8px; margin-bottom: 10px; padding-bottom: 15px; border-bottom: 1px solid rgba(255, 255, 255, 0.06); }
  .dot { width: 12px; height: 12px; border-radius: 50%; }
  .dot-red { background: #FF5F56; } .dot-yellow { background: #FFBD2E; } .dot-green { background: #27C93F; }
  .term-title { font-family: 'JetBrains Mono', monospace; font-size: 14px; color: #64748B; margin-left: 10px; }
  .bullet-list { display: flex; flex-direction: column; gap: 16px; }
  .bullet-item { display: flex; align-items: center; gap: 18px; font-size: 24px; font-weight: 500; line-height: 1.35; color: #E2E8F0; background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.06); padding: 18px 22px; border-radius: 20px; }
  .gradient-text { color: #10B981; font-weight: 800; }
  .arrow { color: #10B981; font-family: 'JetBrains Mono', monospace; font-weight: 700; font-size: 24px; }
  .footer { display: flex; justify-content: space-between; align-items: center; font-size: 20px; font-weight: 600; z-index: 2; }
  .brand { color: #64748B; font-family: 'JetBrains Mono', monospace; }
  .swipe { color: #10B981; font-weight: 700; display: flex; align-items: center; gap: 8px; background: rgba(16, 185, 129, 0.1); padding: 8px 18px; border-radius: 20px; border: 1px solid rgba(16, 185, 129, 0.2); }
</style>
</head>
<body>
  <div class="top-glow"></div>
  <div class="header">
    <div class="badge">$badge</div>
    <div class="counter">$slide_num</div>
  </div>
  <div class="title-section">
    <h1 class="main-title">$title</h1>
  </div>
  <div class="card">
    <div class="window-controls">
      <div class="dot dot-red"></div><div class="dot dot-yellow"></div><div class="dot dot-green"></div>
      <span class="term-title">terminal // render_engine.sh</span>
    </div>
    <div class="bullet-list">$bullets_html</div>
  </div>
  <div class="footer">
    <span class="brand">@infinitus.ai.free</span>
    <span class="swipe">SWIPE &rarr;</span>
  </div>
</body>
</html>
""")

slides_data = [
    {"badge": "Architecture", "slide_num": "01 / 02", "title": "Ollama + Obsidian Core", "bullets": ["<span class='gradient-text'>Direkter Zugriff</span> auf Markdown", "<span class='gradient-text'>Keine Umwege</span> über Cloud-APIs", "Blitzschnelle lokale Verarbeitung"]},
    {"badge": "Execution", "slide_num": "02 / 02", "title": "High-End Masterpiece Look", "bullets": ["<span class='gradient-text'>Terminal-Dark Ästhetik</span> für Creator", "<span class='gradient-text'>Pill-Cards & Neon-Glows</span>", "Perfekt optimiert für Instagram"]}
]

for i, data in enumerate(slides_data, 1):
    bullets_str = "".join([f'<div class="bullet-item"><span class="arrow">&gt;</span><span>{b}</span></div>' for b in data["bullets"]])
    rendered_html = masterpiece_template.substitute(badge=data["badge"], slide_num=data["slide_num"], title=data["title"], bullets_html=bullets_str)
    
    html_filename = os.path.join(OUTPUT_DIR, f"master_slide_{i:02d}.html")
    with open(html_filename, "w", encoding="utf-8") as f:
        f.write(rendered_html)
        
    hti.screenshot(html_file=html_filename, save_as=f"IG_Master_{i:02d}.png")
    print(f"💎 Masterpiece Slide gerendert: IG_Master_{i:02d}.png")

print(f"\n🚀 Alle Slides erfolgreich im Zielordner gespeichert:\n{OUTPUT_DIR}")
