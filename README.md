# Inkwell

A modern desktop creative writing application — manage manuscripts, build worlds, and write alongside Lunaris, your built-in AI companion.

Built with Python, pywebview, TipTap, Three.js, and GSAP.

---

## Getting Started

Inkwell is designed to be completely plug-and-play. No Python, no command line, no dependencies.

1. Download the latest `Inkwell-Setup-x.x.x.exe` from the [Releases](https://github.com/theyoshix/Inkwell/releases) page.
2. Run the installer and launch Inkwell from the Start Menu or desktop shortcut.
3. *Note: Windows SmartScreen may flag the installer on first launch. Click **More info** → **Run anyway**.*

---

## Features

- Full-featured rich-text editor (TipTap) with smart typography, find & replace, typewriter mode, and focus/zen mode
- Chapter binder with drag-to-reorder, status tags, mood tagging, and synopsis
- **Meet Lunaris** — your personal AI writing companion. She reads your World Notes and Character Bible to help brainstorm, review prose, and keep you moving. Runs on a local LLM (LM Studio, Kobold, etc.) or any OpenAI-compatible API.
- Holo-Max visual mode — real-time Three.js sky with aurora, nebula, constellations, shooting stars, and more
- Character Vault, World Notes, Relationship Web, Timeline, and Snapshots satellite windows
- Export to `.docx`, `.epub`, `.txt`, `.md`, `.html`, and Standard Manuscript Format
- Writing stats, streaks, sprint timer, word-frequency heatmap, and personal-best celebrations
- Revision / change tracking with named snapshots and diff view
- Plugin / extension hooks via `window.inkwell` event bus
- Automatic update pipeline

---

## Building from Source

### Requirements

- Python 3.10+
- `pywebview` — `pip install pywebview`
- `python-docx` — `pip install python-docx`
- `ebooklib` — `pip install ebooklib`
- `mammoth` — `pip install mammoth`
- `requests` (optional, used by AI layer) — `pip install requests`

### Run without building

```bash
# 1. Clone
git clone https://github.com/theyoshix/Inkwell.git
cd inkwell

# 2. Install dependencies
pip install pywebview python-docx ebooklib mammoth requests

# 3. Copy and configure the app config
cp inkwell_app_config.example.json inkwell_app_config.json
# Edit inkwell_app_config.json — set ai_api_key if using a cloud AI

# 4. Run
python Inkwell.py
```

### Build the installer

Requires [PyInstaller](https://pyinstaller.org) and [Inno Setup 6](https://jrsoftware.org/isinfo.php).

```bash
pip install pyinstaller
build.bat
```

`build.bat` compiles the exe and, if Inno Setup is installed, packages it into a versioned Windows installer at `dist/Inkwell-Setup-x.x.x.exe`.

---

## Configuration

`inkwell_app_config.json` is gitignored (it contains your API key and local paths).
Use `inkwell_app_config.example.json` as the template.

| Key | Description |
|---|---|
| `ai_mode` | `"local"` or `"openai"` |
| `ai_api_key` | OpenAI / compatible API key (leave blank for local) |
| `ai_local_url` | Local LLM base URL (default: `http://localhost:1234/v1`) |
| `update_check_url` | URL of your hosted `update.json` manifest (optional) |

---

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

---

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

---

## License

MIT
