# Inkwell

A desktop creative writing application built with Python, pywebview, TipTap, Three.js, and GSAP.

## Features

- Full-featured rich-text editor with TipTap
- Chapter binder with drag-to-reorder, status tags, and mood tagging
- AI Copilot (local LLM via LM Studio or OpenAI-compatible API, or cloud via API key)
- Holo-Max visual mode — real-time Three.js sky with aurora, nebula, constellations, and more
- Character Vault, World Notes, Relationship Web, Timeline, and Snapshots satellite windows
- Export to `.docx`, `.epub`, `.txt`, `.md`, `.html`, Standard Manuscript Format
- Writing stats, streaks, sprint timer, word-frequency heatmap
- Plugin / extension hooks via `window.inkwell` event bus
- Automatic update pipeline

## Requirements

- Python 3.10+
- `pywebview` — `pip install pywebview`
- `python-docx` — `pip install python-docx`
- `ebooklib` — `pip install ebooklib`
- `mammoth` — `pip install mammoth`
- `requests` (optional, used by AI layer) — `pip install requests`

## Getting Started

```bash
# 1. Clone
git clone https://github.com/YOUR_USERNAME/inkwell.git
cd inkwell

# 2. Install dependencies
pip install pywebview python-docx ebooklib mammoth requests

# 3. Copy and configure the app config
cp inkwell_app_config.example.json inkwell_app_config.json
# Edit inkwell_app_config.json — set ai_api_key if using cloud AI

# 4. Run
python Inkwell.py
```

## Configuration

`inkwell_app_config.json` is gitignored (it contains your API key and local paths).  
Use `inkwell_app_config.example.json` as the template.

| Key | Description |
|---|---|
| `ai_mode` | `"local"` or `"openai"` |
| `ai_api_key` | OpenAI / compatible API key (leave blank for local) |
| `ai_local_url` | Local LLM base URL (default: `http://localhost:1234/v1`) |
| `update_check_url` | URL of your hosted `update.json` manifest (optional) |

## Update Manifest

Host a JSON file at any public URL:

```json
{
  "version": "1.0.2",
  "download_url": "https://example.com/Inkwell-Setup-1.0.2.exe",
  "release_notes": "Bug fixes and new features."
}
```

Then paste that URL in **Settings → About → Update manifest URL**.

## Project Structure

```
Inkwell.py               — Entry point, window creation
inkwell_api.py           — Python backend API (pywebview JS bridge)
editor_spoke.py          — LLM inference layer
utils.py                 — Asset path helpers
ui/
  main_window.html       — Main editor (TipTap + Three.js + all features)
  character_bible.html   — Character Vault satellite window
  world_notes.html       — World Notes satellite window
  relationship_web.html  — Relationship Web canvas satellite
  timeline.html          — Timeline / story arc board satellite
  snapshots.html         — Revision snapshots satellite
  stats_window.html      — Writing statistics dashboard
  project_dashboard.html — Multi-project manager
  splash.html            — Startup splash screen
```

## License

MIT
