# Inkwell — TODO (Priority Order)

Items are sequenced so each phase builds on a stable foundation from the one before it.
No phase should begin until the previous one is solid.

---

## ✅ Done
- [x] Time-of-day tinting (dawn/dusk/night) — ambient event system
- [x] Ambient event system (sun/moon, eclipse, aurora, black hole, constellations, nebula, plasma tendrils)
- [x] Drag-to-reorder chapters in the binder
- [x] Smooth chapter transitions — GSAP flash + edge-pulse sweep
- [x] Scroll-based chapter auto-selection (50% viewport threshold)

---

## Phase 1 — Stability & Data Safety
*Nothing else matters if users lose work.*

- [x] **Crash recovery** — rolling checkpoint written every 60s; on launch detect corrupted/missing project and offer restore with timestamp
- [x] **Auto-save indicator** — pulsing cyan dot = saving, solid green = saved, red = failed (with hover error tooltip in title bar)
- [x] **Backup to folder** — user-chosen path, keeps last N timestamped copies; separate from crash checkpoints

---

## Phase 2 — Core UX Polish
*The app should feel completely native and intentional before adding features.*

- [x] **Suppress all native browser/OS chrome** — `outline:none` on focus for all buttons/inputs; no white squares on tab/esc, no default selection highlights, no scrollbar gutter flicker; zero Windows/Chrome bleed-through
- [x] **Custom themed scrollbar** — picks up CSS variables, replaces OS default in all scroll containers
- [x] **Custom tooltips** — themed tooltip system (replaces browser `title=`); dark card in normal mode; scanline/glow panel in holo/holo-max; context-sensitive content (word count on chapter cards, model name on copilot button, shortcut hint on toolbar icons)
- [x] **Context menus** — right-click in editor, binder, character vault, world notes triggers a fully themed menu; normal: dark frosted card; holo-max: holographic scanline panel; items are context-sensitive (chapter → Rename / Duplicate / Delete / Status; text selection → Copy / Rephrase / Add to Context; binder bg → New Chapter / Import)
- [x] **Settings modal overhaul** — tabbed: General (language, autosave interval, font size), Appearance (theme picker, holo intensity, background opacity), Writing (word goal, typewriter mode, focus mode), Copilot (model, temperature, max tokens, system prompt), About (version, licenses); holo tabs get scanline accent

---

## Phase 3 — Writing Core
*Daily-use features a writer reaches for every session.*

- [x] **Smart typography** — auto-convert straight quotes → curly, `--` → em-dash, `...` → ellipsis; toggle per-project in settings; never fires inside code blocks or lore fields
- [x] **Find & Replace** — Ctrl+H panel; plain text, case-sensitive, and regex modes; live match highlights; chapter scope or full-manuscript scope toggle
- [x] **Typewriter mode** — keeps the active line vertically centered as you type
- [x] **Focus / Zen mode** — hides binder, copilot, toolbar; one hotkey (Ctrl+\) to toggle
- [x] **Chapter synopsis** — collapsible one-liner per chapter stored alongside content; shown in binder tooltip and passed to copilot as structural context
- [x] **Reading / proofread mode** — strips all UI chrome except a slim exit button; clean single-column view, larger line-height, sepia or white background; no editing
- [x] **Keyboard shortcut map** — `?` modal listing all hotkeys; themed

---

## Phase 4 — Navigation & Structure
*Help writers move through longer works without losing their place.*

- [x] **Quick-jump palette (Ctrl+K)** — fuzzy search across chapters, characters, world notes
- [x] **Command palette (Ctrl+Shift+P)** — action launcher: New Chapter, Toggle Theme, Run Export, Open Character Vault, Jump to Chapter N…; fuzzy-searchable, keyboard-navigable, fully themed
- [x] **Chapter status tags** — Draft / Revising / Done as colored dots on binder entries; set via context menu
- [x] **Chapter mood tagger** — assign emotional tone (Tense / Melancholy / Euphoric / Mysterious / Dread / Wonder) via right-click; binder card gets a subtle colour wash; tone fed to copilot as context hint
- [x] **World Notes search** — full-text search bar at top of World Notes satellite; highlights matching entries; filters sidebar categories live

---

## Phase 5 — Statistics & Goals
*Keep the writer motivated with feedback on progress.*

- [x] **Ambient word goal** — session/daily target with quiet background fill as you write
- [x] **Chapter progress bar** — word-count ring/bar on each binder card
- [x] **Writing stats dashboard** — satellite window: daily/weekly/all-time word counts, average session WPM, longest streak, time-of-day productivity heatmap; lightweight canvas charts
- [x] **Writing streak tracker** — consecutive days hitting goal shown on welcome screen with flame icon; resets at midnight; stored in app config
- [x] **Distraction score overlay** — floating badge counting time since last keypress; pulses after 3 min idle, vanishes on next keystroke; holo-max: holographic HUD readout
- [x] **Personal best celebrations** — track longest session, fastest WPM, most words in a day; holo-max fires special ambient event on PB; subtle toast in other modes

---

## Phase 6 — Export & Import
*Writers need to get their work out and in.*

- [x] **Export polish** — chapter range selector, scene-break symbol chooser (`***` / `•` / `───`), optional front-matter block, export to `.docx` with proper styles, `.epub` for e-readers
- [x] **Manuscript formatting preset** — one-click Standard Manuscript Format: Courier 12pt, double-spaced, 1-inch margins, header with Author / Title / Page#
- [x] **Import** — `.docx` via mammoth.js, Markdown (`.md`), Fountain (`.fountain`); preview step before committing to a chapter
- [x] **Project templates** — on New Project: Novel (acts + chapters), Short Story (single chapter), Screenplay (Fountain structure), World-building Bible (lore-first)
- [x] **Multi-project dashboard** — full-screen project manager: grid of project cards with cover art, last-modified, word count, status badge; search/filter bar

---

## Phase 7 — Copilot Enhancements
*Deepen the AI layer once the writing surface is solid.*

- [x] **Inline ghost-text suggestions** — accept with Tab
- [x] **Slash commands in the editor** — `/suggest`, `/continue`, `/rephrase` on surrounding paragraph
- [x] **Pinned context snippets** — drag a character card or lore note into copilot as active context
- [x] **Character voice profiles** — "Voice & Tone" field per character card; auto-injects into system prompt when that character appears in the active chapter
- [x] **Style mirror** — copilot analyses the last ~2000 words of the user's prose (sentence length, adverb density, dialogue ratio) and silently prepends a style description so suggestions blend in
- [x] **AI consistency checker** — on-demand batch scan; flags potential continuity errors (attribute changes, timeline gaps, location contradictions); results in a dedicated review panel
- [x] **Writing sprint timer** — Pomodoro-style countdown (25/15/custom min); tracks sprint word count; completion card at end; holo-max: holographic countdown ring near dock

---

## Phase 8 — Satellite Windows
*Expand the workspace for complex projects.*

- [x] **Satellite auto-restore** — reopen whichever satellite windows were open on last close
- [x] **Character relationship web** — nodes per character, drag-connectable edges with labels (Ally / Rival / Lover / Family); force-directed spring layout on Canvas; holo-aware styling
- [x] **Timeline / story arc board** — horizontal swimlane per POV character; chapters as draggable cards; colour-coded by POV; syncs chapter order back to binder
- [x] **Lore link hover cards** — hover a known name in manuscript to see mini Character/World card

---

## Phase 9 — Revision & Advanced Writing
*Power-user features for serious editing passes.*

- [x] **Revision / change tracking** — named snapshot saves ("Before Edit Pass 2"); diff view with green additions / red deletions against any snapshot; stored alongside project file
- [x] **Word frequency heatmap** — optional manuscript overlay; overused words above a threshold get a soft warning tint; toggle in settings; rolling per-session frequency map

---

## Phase 10 — Holo-Max Visual Upgrades
*Polish the spectacle once all functional layers are complete.*

- [x] **Shooting stars** — rare fast streak events, 1–3 per activation, fade trail via `Line` geometry; night-boosted, 2–4s, long cooldown
- [x] **Nebula colour drift** — primary nebula slowly cycles hue over 5–10 min via slow `sin` on colour mix uniform; always-on, imperceptible moment-to-moment
- [x] **Floor ripple on milestone** — second concentric ring on every 500-word milestone, larger radius, magenta accent, distinct from per-keystroke ripple
- [x] **Camera tilt on drag** — on max upward drag, subtle FOV squeeze (58°→52°) to sell "looking up at sky"; lerps back on release
- [x] **Depth-of-field blur** — subtle DOF shader pass; far geometry (z ≈ −50) blurs slightly, focuses as camera drags toward it
- [x] **Horizon lightning** — rare silent lightning flash across the ghost-city skyline; bright horizontal streak + 3-frame bloom spike then fade
- [x] **Weather layer** — random "digital static burst" that washes the scene in full-screen noise then clears; shader post-process, 3–8s, rare trigger
- [x] **Wormhole / portal pull** — occasional deep-background UV distortion that stretches the portal ring into a tunnel for 10–20s then snaps back
- [x] **Interactive satellite** — clicking the orbiting satellite triggers a particle burst and spirals it to a new orbit; Easter egg
- [x] **Constellation labels** — faint floating labels near each constellation cluster when camera tilts up during a constellation event
- [x] **Seasonal palette mode** — in-story season set in settings; shifts palette and event weights (Winter: cooler blues, aurora +50%; Summer: warm sun, more lens flare; Autumn: amber fog; Spring: brighter nebula)

---

## Phase 11 — Infrastructure & Extensibility
*Long-tail items that pay off at scale.*

- [x] **Plugin / extension hooks** — lightweight JS event bus: `inkwell.on('chapter:save', fn)`, `inkwell.register('copilot:provider', {…})`; lets power users swap AI providers or export targets without forking core

---

## Phase 12 — Performance
*Systematic profiling and optimization pass once the full feature set is known.*

- [x] **Profile and baseline** — `window.inkwell.perf.report()` from console snapshots frame timing, DOM node counts, live TipTap instances, JS heap, holo mode, season
- [x] **Rendering bottlenecks** — fixed `getBoundingClientRect()` → ResizeObserver cache in electricity arcs; increased elec cooldown 80→120ms; underlay debounce 200→350ms; replaced `filter()` with reverse-scan in WPM/emotion hot path; `body.is-typing` class collapses 3-layer text-shadow to single layer during active typing
- [x] **DOM size audit** — single live TipTap editor architecture already ensures only one ProseMirror tree is mounted at a time; `inkwell.perf.domStats()` exposes node counts for ongoing monitoring
- [x] **WebGL scene budget** — ambient alpha uniforms skip GPU upload when delta < 0.0008; nebula hueDrift throttled to 15 Hz (every 4 frames) saving 75% of the `Math.sin` + uniform upload cost
- [x] **Memory leak audit** — ResizeObserver disconnected in `_unmountEditor`; TipTap `ed.destroy()` already called on every chapter switch; `inkwell.perf.memStats()` exposes JS heap for heap-snapshot baseline
- [x] **CSS paint cost audit** — `[data-style="holo-max"] body.is-typing .ProseMirror` collapses expensive 3-layer text-shadow to single layer during active typing; backdrop-filter already restricted to active-paper only
- [x] **Startup time** — ambient system init staggered 80ms after data-streams init so boot sequence and grid render complete before the heavier ambient object allocation begins

---

## Phase 13 — Polish & Housekeeping

- [x] **Emoji purge** — all 🌍📌🗑📖🕸✏ etc. replaced with clean inline SVG icons or geometric Unicode symbols across main_window, relationship_web, world_notes, and character_bible
- [x] **Custom tooltips** — themed tooltip system added to world_notes and character_bible (replaces native `title=`); dark card in normal mode, cyan-glow in holo; 280ms delay, smart edge-clamping
- [x] **Relationship web drag rework** — drag node center to move; drag node outer ring to draw a live connection wire to another node; click-vs-drag threshold prevents accidental info-card on drag; crosshair cursor on connection ring zone
- [x] **Update pipeline** — `APP_VERSION` constant + `check_for_updates()` / `download_and_install_update()` in `inkwell_api.py`; sticky update banner in main window; About tab shows live version, update status, and configurable manifest URL; startup auto-check at 10 s
