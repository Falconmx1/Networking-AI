#!/bin/bash
# Networking AI - Instalador para Linux

set -e

echo "╔════════════════════════════════════╗"
echo "║   Networking AI - Instalador Linux ║"
echo "╚════════════════════════════════════╝"

# Detectar distribución
if [ -f /etc/debian_version ]; then
    echo "[*] Distribución Debian/Ubuntu detectada"
    sudo apt update
    sudo apt install -y python3 python3-pip tcpdump net-tools
elif [ -f /etc/redhat-release ]; then
    echo "[*] Distribución RedHat/Fedora detectada"
    sudo dnf install -y python3 python3-pip tcpdump net-tools
else
    echo "[!] Distribución no soportada automáticamente"
    echo "[*] Instala manualmente: python3, pip, tcpdump"
fi

# Instalar Npcap compatible (via wine si es necesario)
echo "[*] Instalando dependencias Python"
pip3 install -r requirements.txt

# Dar permisos de ejecución
chmod +x src/cli/main.py

# Crear enlace simbólico global
sudo ln -sf $(pwd)/src/cli/main.py /usr/local/bin/netai

echo "[✓] Instalación completada!"
echo "[*] Ejecuta 'netai monitor --packets 10' para probar"
