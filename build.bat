@echo off
:: ─────────────────────────────────────────────────────────────────────────────
:: Inkwell full build pipeline
::
:: Step 1 — PyInstaller  →  dist\Inkwell.exe          (bundled app)
:: Step 2 — Inno Setup   →  dist\Inkwell-Setup-X.X.X.exe  (installer)
::
:: Usage:  build.bat
::
:: Requires:
::   pip install pyinstaller
::   Inno Setup 6 from https://jrsoftware.org/isdl.php
:: ─────────────────────────────────────────────────────────────────────────────
setlocal

set ISCC="C:\Program Files (x86)\Inno Setup 6\ISCC.exe"

:: ── Read version from inkwell_api.py ─────────────────────────────────────────
for /f "tokens=3 delims= " %%v in ('findstr /r "^APP_VERSION" inkwell_api.py') do set RAW=%%v
set VERSION=%RAW:'=%
echo.
echo ═══════════════════════════════════════════
echo   Inkwell Build Pipeline  v%VERSION%
echo ═══════════════════════════════════════════
echo.

:: ── Step 1: PyInstaller ──────────────────────────────────────────────────────
echo [1/2] PyInstaller — bundling app...
echo.

if exist dist\Inkwell.exe del /q dist\Inkwell.exe

pyinstaller Inkwell.spec --noconfirm
if errorlevel 1 (
    echo.
    echo [FAIL] PyInstaller step failed.
    exit /b 1
)

if not exist dist\Inkwell.exe (
    echo.
    echo [FAIL] dist\Inkwell.exe not produced.
    exit /b 1
)

echo.
echo [OK]   dist\Inkwell.exe produced.
echo.

:: ── Step 2: Inno Setup ───────────────────────────────────────────────────────
echo [2/2] Inno Setup — building installer...
echo.

if not exist %ISCC% (
    echo [SKIP] Inno Setup not found at %ISCC%
    echo        Download from: https://jrsoftware.org/isdl.php
    echo        Then re-run build.bat to produce the installer.
    echo.
    echo        Standalone exe is at: dist\Inkwell.exe
    goto :done
)

%ISCC% installer.iss
if errorlevel 1 (
    echo.
    echo [FAIL] Inno Setup step failed.
    exit /b 1
)

echo.
echo [OK]   dist\Inkwell-Setup-%VERSION%.exe produced.

:done
echo.
echo ───────────────────────────────────────────
echo   Build complete!
echo ───────────────────────────────────────────
echo.
endlocal
