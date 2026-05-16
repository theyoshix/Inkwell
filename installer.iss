; ─────────────────────────────────────────────────────────────────────────────
; Inkwell — Inno Setup installer script
;
; Prerequisites:
;   1. Run build.bat first (produces dist\Inkwell.exe via PyInstaller)
;   2. Then: "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer.iss
;      (build.bat does both steps automatically if Inno Setup is installed)
;
; Output:  dist\Inkwell-Setup-{version}.exe
; ─────────────────────────────────────────────────────────────────────────────

#define AppName      "Inkwell"
#define AppPublisher "Cecil & Lunaris"
#define AppURL       "https://github.com/Yoshix/inkwell"
#define ExeFile      "dist\Inkwell.exe"

; Read version from the built exe's ProductVersion resource
#define AppVersion   GetFileProductVersion(ExeFile)

[Setup]
AppId={{A1B2C3D4-E5F6-7890-ABCD-EF1234567890}
AppName={#AppName}
AppVersion={#AppVersion}
AppPublisher={#AppPublisher}
AppPublisherURL={#AppURL}
AppSupportURL={#AppURL}
AppUpdatesURL={#AppURL}

; Install to C:\Program Files\Inkwell
DefaultDirName={autopf}\{#AppName}
DefaultGroupName={#AppName}
AllowNoIcons=yes

; Installer appearance
SetupIconFile=favicon.ico
WizardStyle=modern
WizardSmallImageFile=favicon.ico

; Output
OutputDir=dist
OutputBaseFilename=Inkwell-Setup-{#AppVersion}
Compression=lzma2/ultra64
SolidCompression=yes
InternalCompressLevel=ultra64

; Require admin so we can write to Program Files
PrivilegesRequired=admin
PrivilegesRequiredOverridesAllowed=dialog

; Minimum Windows version: Windows 10 (required for Edge WebView2)
MinVersion=10.0

; Uninstall info shown in Add/Remove Programs
UninstallDisplayName={#AppName}
UninstallDisplayIcon={app}\Inkwell.exe

; Allow running the app directly after install
CloseApplications=yes
CloseApplicationsFilter=Inkwell.exe

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
; Desktop shortcut is opt-in (checked by default)
Name: "desktopicon"; Description: "Create a &desktop shortcut"; \
    GroupDescription: "Additional icons:"; Flags: checked

[Files]
; The single bundled executable — that's all we need
Source: "dist\Inkwell.exe"; DestDir: "{app}"; \
    DestName: "Inkwell.exe"; Flags: ignoreversion

; Include favicon for the uninstaller entry icon
Source: "favicon.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
; Start Menu
Name: "{group}\{#AppName}";           Filename: "{app}\Inkwell.exe"; IconFilename: "{app}\favicon.ico"
Name: "{group}\Uninstall {#AppName}"; Filename: "{uninstallexe}"

; Desktop (only if the task was selected)
Name: "{commondesktop}\{#AppName}"; Filename: "{app}\Inkwell.exe"; \
    IconFilename: "{app}\favicon.ico"; Tasks: desktopicon

[Registry]
; Register as a known app so Windows "Open with" can find it
Root: HKLM; Subkey: "Software\{#AppPublisher}\{#AppName}"; \
    ValueType: string; ValueName: "InstallPath"; ValueData: "{app}"; Flags: uninsdeletekey

[Run]
; Offer to launch Inkwell at the end of setup
Filename: "{app}\Inkwell.exe"; \
    Description: "Launch {#AppName}"; \
    Flags: nowait postinstall skipifsilent

[UninstallDelete]
; Clean up app data only if the user confirms in the uninstaller
; (projects are stored elsewhere — this just removes the install folder)
Type: filesandordirs; Name: "{app}"

[Code]
// ── Check for Edge WebView2 runtime (required by pywebview) ──────────────────
function WebView2IsInstalled(): Boolean;
var
  ver: String;
begin
  Result := RegQueryStringValue(
    HKLM,
    'SOFTWARE\WOW6432Node\Microsoft\EdgeUpdate\Clients\{F3017226-FE2A-4295-8BDF-00C3A9A7E4C5}',
    'pv', ver
  ) and (ver <> '') and (ver <> '0.0.0.0');
  if not Result then
    Result := RegQueryStringValue(
      HKLM,
      'SOFTWARE\Microsoft\EdgeUpdate\Clients\{F3017226-FE2A-4295-8BDF-00C3A9A7E4C5}',
      'pv', ver
    ) and (ver <> '') and (ver <> '0.0.0.0');
end;

function InitializeSetup(): Boolean;
begin
  Result := True;
  if not WebView2IsInstalled() then begin
    if MsgBox(
      'Inkwell requires the Microsoft Edge WebView2 Runtime, which was not found on this machine.'
      + #13#10#13#10
      + 'It is included with Windows 10 (version 1803+) and Windows 11. '
      + 'If you are on an older version, please download it from:'
      + #13#10
      + 'https://developer.microsoft.com/en-us/microsoft-edge/webview2/'
      + #13#10#13#10
      + 'Continue installing Inkwell anyway?',
      mbConfirmation, MB_YESNO
    ) = IDNO then
      Result := False;
  end;
end;
