# Installation du studio sous Windows 10/11 64 bits via winget (paquets officiels signés).
#   -Plan : affiche ce qui serait fait, n'exécute rien
#   -Yes  : n'attend pas de confirmation
# Unreal Engine lui-même s'installe depuis l'Epic Games Launcher (compte Epic de l'humain).
param([switch]$Plan, [switch]$Yes)
$ErrorActionPreference = "Stop"

function Run($cmd) { if ($Plan) { Write-Host "   [plan] $cmd" } else { Write-Host "▸ $cmd"; Invoke-Expression $cmd } }

if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
  Write-Host "winget requis (App Installer, Microsoft Store)."; exit 1
}

# Vérifications matérielles (lecture seule)
$ramGB = [math]::Round((Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory / 1GB)
$gpu   = (Get-CimInstance Win32_VideoController | Select-Object -First 1).Name
$free  = [math]::Round((Get-PSDrive C).Free / 1GB)
Write-Host "Matériel : RAM $ramGB Go · GPU $gpu · disque C: libre $free Go"
if ($ramGB -lt 32) { Write-Warning "32 Go de RAM recommandés pour Unreal Engine 5.8 (minimum pratique 16 Go)." }
if ($free -lt 300) { Write-Warning "Au moins 300 Go libres recommandés (moteur + cache + projet)." }

Write-Host "`n▸ Plan d'installation"
if (-not $Plan -and -not $Yes) { $r = Read-Host "Continuer ? [o/N]"; if ($r -notmatch '^[oOyY]$') { exit 0 } }

Run "winget install --id EpicGames.EpicGamesLauncher -e --accept-package-agreements"
Run "winget install --id Microsoft.VisualStudio.2022.Community -e --override '--quiet --wait --add Microsoft.VisualStudio.Workload.NativeGame --add Microsoft.VisualStudio.Workload.NativeDesktop --includeRecommended'"
Run "winget install --id Microsoft.DotNet.SDK.8 -e"
Run "winget install --id Git.Git -e"
Run "winget install --id GitHub.GitLFS -e"
Run "winget install --id GitHub.cli -e"
Run "winget install --id Python.Python.3.12 -e"
Run "winget install --id OpenJS.NodeJS.LTS -e"
Run "winget install --id Gyan.FFmpeg -e"
Run "winget install --id BlenderFoundation.Blender -e"
Run "winget install --id GrafanaLabs.k6 -e"
Run "winget install --id Gitleaks.Gitleaks -e"
Run "py -m pip install --user semgrep robotframework robotframework-browser jsonschema"
Run "rfbrowser init"
Run "git lfs install"

Write-Host "`n▸ Étapes manuelles (humain) :"
Write-Host "  1. Ouvrir Epic Games Launcher, se connecter, installer Unreal Engine 5.8 (cible Windows + symboles de débogage)."
Write-Host "  2. Dans Claude Code : /plugin install unreal-engine-skills-for-claude-code@claude-plugins-official"
Write-Host "  3. Dans l'éditeur : activer les plugins 'Model Context Protocol' et 'AllToolsets', puis console : ModelContextProtocol.StartServer"
Write-Host "  4. Définir UE_ROOT (ex. setx UE_ROOT ""C:\Program Files\Epic Games\UE_5.8"")"
Write-Host "  5. Vérifier : py tools\doctor.py"
Write-Host "`nLicence Visual Studio Community : gratuite pour particuliers et petites structures — vérifiez les conditions Microsoft pour votre cas."
