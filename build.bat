@echo off
:: ─────────────────────────────────────────────────────────────────────────────
:: Inkwell build script
:: Usage:  build.bat
:: Output: dist\Inkwell.exe
:: ─────────────────────────────────────────────────────────────────────────────

:: Read current version from inkwell_api.py
for /f "tokens=3 delims= " %%v in ('findstr /r "^APP_VERSION" inkwell_api.py') do (
    set RAW=%%v
)
:: Strip surrounding quotes
set VERSION=%RAW:'=%
echo Building Inkwell v%VERSION%...

:: Clean previous build artefacts
if exist dist\Inkwell.exe del /q dist\Inkwell.exe

:: Run PyInstaller
pyinstaller Inkwell.spec --noconfirm

if errorlevel 1 (
    echo.
    echo [ERROR] Build failed.
    exit /b 1
)

echo.
echo [OK] dist\Inkwell.exe  --  Inkwell v%VERSION%
echo.
