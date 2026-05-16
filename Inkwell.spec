# -*- mode: python ; coding: utf-8 -*-
#
# PyInstaller spec for Inkwell
# Build with:  pyinstaller Inkwell.spec
#
# Output:  dist/Inkwell.exe   (single-file, no console, with custom icon)

import os
from PyInstaller.utils.hooks import collect_submodules

block_cipher = None

# ── Data files bundled into the exe ───────────────────────────────────────────
#   Each tuple: (source_glob_or_path, destination_folder_inside_bundle)
datas = [
    ('ui',                    'ui'),           # All HTML satellite windows
    ('favicon.ico',           '.'),            # App icon (also used by pywebview)
    ('Open Manuscript Screen.png', '.'),       # Welcome screen art
]

# Include Lunaris Avatar if it exists (optional override art)
if os.path.exists('Lunaris Avatar.png'):
    datas.append(('Lunaris Avatar.png', '.'))

# ── Hidden imports ─────────────────────────────────────────────────────────────
hiddenimports = [
    'webview',
    'webview.platforms.winforms',
    'clr',
    'pythonnet',
    'docx',
    'docx.oxml',
    'docx.oxml.ns',
    'ebooklib',
    'ebooklib.epub',
    'mammoth',
    'html.parser',
    'urllib.request',
    'webbrowser',
    'threading',
    'tempfile',
]

a = Analysis(
    ['Inkwell.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tkinter', 'matplotlib', 'numpy', 'pandas',
        'scipy', 'PIL', 'cv2', 'PyQt5', 'PyQt6',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Inkwell',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,                          # Compress with UPX if available
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,                     # No console window
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='favicon.ico',                # ← THIS sets the .exe icon in Explorer
    version='version_info.txt',        # ← Windows version metadata (see below)
)
