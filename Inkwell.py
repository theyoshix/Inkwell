#!/usr/bin/env python3
"""
Inkwell - Creative Writing Application
Entry point: wires together the API, HTML, and PyWebView windows.
"""

import os
import sys
import subprocess
import webview
from utils import get_asset_path, load_image_to_base64
from inkwell_api import Inkwell, APP_VERSION

# GLOBAL STEALTH PATCH: Prevents background processes from flashing console windows
if os.name == 'nt':
    class StealthPopen(subprocess.Popen):
        def __init__(self, *args, **kwargs):
            kwargs['creationflags'] = subprocess.CREATE_NO_WINDOW | kwargs.get('creationflags', 0)
            super().__init__(*args, **kwargs)
    subprocess.Popen = StealthPopen


def _load_html(filename):
    """Load an HTML file from the ui/ subdirectory."""
    filepath = get_asset_path(os.path.join('ui', filename))
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def create_splash_html(api):
    """Load splash.html and inject the saved holo mode so the correct skin
    activates before the first frame — no localStorage, no async, no flash."""
    html = _load_html('splash.html')
    saved_mode = getattr(api, 'holo_mode', 'off')
    # Insert a tiny script as the very first thing inside <head> so it runs
    # before any CSS paint and before the rest of the JS block.
    inject = f'<script>window._injectedHoloMode = "{saved_mode}";</script>\n'
    html = html.replace('<meta charset="UTF-8">', '<meta charset="UTF-8">\n' + inject, 1)
    return html


def create_ui(api):
    """Builds the main editor window HTML, injecting the splash image and saved holo mode."""
    html = _load_html('main_window.html')
    lunaris_b64 = load_image_to_base64("Open Manuscript Screen.png")
    if lunaris_b64:
        html = html.replace("LUNARIS_START_IMAGE_PLACEHOLDER", lunaris_b64)
    # Dock avatar — uses "Lunaris Avatar.png" if it exists, otherwise falls back to the same art
    avatar_b64 = load_image_to_base64("Lunaris Avatar.png") or lunaris_b64 or ""
    html = html.replace("LUNARIS_DOCK_IMAGE_PLACEHOLDER", avatar_b64)
    # Inject saved holo mode as a synchronous window variable so the welcome screen
    # can apply the correct skin before the first frame — no localStorage, no async flash.
    saved_mode = getattr(api, 'holo_mode', 'off')
    inject = f'<script>window._injectedHoloMode = "{saved_mode}";</script>\n'
    html = html.replace('<meta charset="UTF-8">', '<meta charset="UTF-8">\n' + inject, 1)
    return html

def main():
    """Main entry point"""
    print("=" * 50)
    print("Inkwell - Starting...")
    print(f"Version {APP_VERSION}")
    print("=" * 50)

    api = Inkwell()

    import ctypes
    import threading # <-- Required for our timer

    try:
        user32 = ctypes.windll.user32
        screen_width  = user32.GetSystemMetrics(0)
        screen_height = user32.GetSystemMetrics(1)
    except:
        screen_width, screen_height = 1920, 1080

    window_width, window_height = 1400, 900
    x = (screen_width  - window_width)  // 2
    y = (screen_height - window_height) // 2

    splash_size = 400
    splash_x = (screen_width - splash_size) // 2
    splash_y = (screen_height - splash_size) // 2

    print(f"Screen: {screen_width}x{screen_height}  -->  Window at ({x}, {y})")

    # ==========================================
    # 1. THE MAIN EDITOR (Starts Hidden)
    # ==========================================
    main_window = webview.create_window(
        'Inkwell',
        html=create_ui(api),
        js_api=api,
        width=window_width,
        height=window_height,
        x=x,
        y=y,
        resizable=True,
        frameless=True,
        easy_drag=False,
        background_color='#1A1D23',
        hidden=True       # <--- Builds silently in the background
    )
    api._window = main_window

    # ==========================================
    # 2. THE SPLASH SCREEN (Transparent & Frameless)
    # ==========================================
    splash_window = webview.create_window(
        'Splash',
        html=create_splash_html(api),
        width=splash_size,
        height=splash_size,
        x=splash_x,        # <--- FIX: Centers the logo horizontally
        y=splash_y,        # <--- FIX: Centers the logo vertically
        frameless=True,
        transparent=True,  # <--- Crucial: Drops the OS window frame
        on_top=True
    )

    # ==========================================
    # 3. THE HANDOFF LOGIC
    # ==========================================
    def transition_to_main():
        splash_window.destroy()
        main_window.show()

    def on_splash_loaded():
        # Start a 2.0 second timer, then trigger the transition
        threading.Timer(2.0, transition_to_main).start()

    splash_window.events.loaded += on_splash_loaded

    # --- HIVE MIND: SYNC MINIMIZE & RESTORE ---
    def sync_minimize():
        import webview
        for w in webview.windows:
            if w.title != 'Inkwell' and w.title != 'Splash':
                w.minimize()

    def sync_restore():
        import webview
        for w in webview.windows:
            if w.title != 'Inkwell' and w.title != 'Splash':
                w.restore()

    def on_app_closing():
        """Gracefully close all satellite windows before the main engine shuts down"""
        import webview
        for w in list(webview.windows):
            if w.title != 'Inkwell' and w.title != 'Splash':
                try:
                    w.destroy()
                except:
                    pass
        return True 
                
    main_window.events.closing += on_app_closing
    main_window.events.minimized += sync_minimize
    main_window.events.restored += sync_restore

    webview.start(debug=False)


if __name__ == "__main__":
    main()