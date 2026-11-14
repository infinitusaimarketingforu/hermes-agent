import os
import re
import requests
import json
import subprocess

# CONFIGURATION
OBSIDIAN_VAULT_PATH = r"C:\Users\elvis\.hermes\Obsidian Vault.md"  # Pfad zu deinem Vault
LTX_API_URL = "https://api.ltx.io/v1/generate"            # LTX 2.5 API
LTX_API_KEY = "ltxv_bqiwATc9dDWVB8mRca4x5qmW8KxZafOVs72cvwVLWNw"                         # LTX API Key
N8N_WEBHOOK_URL = "http://localhost:5678/webhook/auto-publish"

def parse_obsidian_markdown(file_name):
    """Liest die Obsidian .md Datei aus und extrahiert Skript & Visuals."""
    file_path = os.path.join(OBSIDIAN_VAULT_PATH, file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extrahiere z.B. Hooks, Visual Prompts und Text Overlays aus den MD-Dateien
    title_match = re.search(r'Title Template:\s*"(.*?)"', content)
    hook_match = re.search(r'\[0-2s HARD HOOK\]\s*"(.*?)"', content)
    visual_match = re.search(r'\(Visual:\s*(.*?)\)', content)

    title = title_match.group(1) if title_match else "AI Automation Update"
    hook = hook_match.group(1) if hook_match else "Dein Webhook schlägt fehl!"
    visual_prompt = visual_match.group(1) if visual_match else "Terminal dark background #0A0A0F, green text #10B981"

    return {
        "title": title,
        "hook": hook,
        "visual_prompt": f"Terminal-Dark design, #0A0A0F background, #10B981 green accent, {visual_prompt}"
    }

def generate_ltx_video(prompt):
    """Fordert das Video vom LTX 2.5 Model an."""
    headers = {
        "Authorization": f"Bearer {LTX_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": prompt,
        "model": "ltx-2.5",
        "duration_seconds": 5,
        "aspect_ratio": "9:16"
    }
    response = requests.post(LTX_API_URL, json=payload, headers=headers)
    video_url = response.json().get("video_url")
    
    # Video lokal herunterladen
    video_data = requests.get(video_url).content
    raw_video_path = "temp_raw_video.mp4"
    with open(raw_video_path, "wb") as f:
        f.write(video_data)
        
    return raw_video_path

def render_final_video_ffmpeg(raw_video_path, overlay_text, output_path="final_reel.mp4"):
    """Nutzt FFmpeg auf deinem PC für den Terminal-Dark Style (Text & Overlay)."""
    ffmpeg_cmd = [
        "ffmpeg", "-y", "-i", raw_video_path,
        "-vf", f"drawtext=text='{overlay_text}':fontcolor=white:fontsize=36:x=(w-text_w)/2:y=(h-text_h)/2:font='JetBrains Mono'",
        "-c:a", "copy", output_path
    ]
    subprocess.run(ffmpeg_cmd, check=True)
    return output_path

def send_to_n8n(final_video_path, metadata):
    """Sendet das fertige Video + Titel & Captions an deinen n8n Auto-Publisher."""
    files = {'video': open(final_video_path, 'rb')}
    data = {'title': metadata['title'], 'caption': metadata['hook']}
    requests.post(N8N_WEBHOOK_URL, files=files, data=data)
    print("🚀 Video erfolgreich an n8n Auto-Publisher übergeben!")

if __name__ == "__main__":
    # Beispiel: Lies 'Woche-6-Content-Plan.md' direkt aus Obsidian aus
    md_file = "Woche-6-Content-Plan.md"
    parsed_data = parse_obsidian_markdown(md_file)
    
    print(f"📄 Verarbeite Obsidian Notiz: {md_file}")
    print(f"🎬 Generiere LTX 2.5 Video für Visual: {parsed_data['visual_prompt']}")
    
    raw_video = generate_ltx_video(parsed_data['visual_prompt'])
    final_video = render_final_video_ffmpeg(raw_video, parsed_data['hook'])
    
    send_to_n8n(final_video, parsed_data)