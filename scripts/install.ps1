# Networking AI - Instalador para Windows
Write-Host "╔════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║   Networking AI - Instalador Windows ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════╝" -ForegroundColor Cyan

# Verificar Python
$pythonInstalled = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonInstalled) {
    Write-Host "[!] Python no encontrado. Descargando..." -ForegroundColor Yellow
    Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.11.7/python-3.11.7-amd64.exe" -OutFile "$env:TEMP\python.exe"
    Start-Process -Wait "$env:TEMP\python.exe" "/quiet InstallAllUsers=1 PrependPath=1"
}

# Instalar Npcap (necesario para Scapy en Windows)
$npcapInstalled = Test-Path "C:\Program Files\Npcap"
if (-not $npcapInstalled) {
    Write-Host "[!] Instalando Npcap..." -ForegroundColor Yellow
    Invoke-WebRequest -Uri "https://npcap.com/dist/npcap-1.79.exe" -OutFile "$env:TEMP\npcap.exe"
    Start-Process -Wait "$env:TEMP\npcap.exe" "/S"
}

# Instalar dependencias Python
Write-Host "[*] Instalando dependencias Python..." -ForegroundColor Green
pip install -r requirements.txt

# Crear acceso directo
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$Home\Desktop\Networking AI.lnk")
$Shortcut.TargetPath = "cmd.exe"
$Shortcut.Arguments = "/k python `"$pwd\src\cli\main.py`""
$Shortcut.Save()

Write-Host "[✓] Instalación completada!" -ForegroundColor Green
Write-Host "[*] Ejecuta 'python src/cli/main.py monitor'" -ForegroundColor Cyan
