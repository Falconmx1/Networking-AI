"""Captura de paquetes multiplataforma con Scapy"""
import platform
from scapy.all import sniff, IP, TCP, UDP

class PacketCapture:
    def __init__(self, interface=None):
        self.interface = interface
        self.os_type = platform.system()
        self.packets = []
    
    def packet_callback(self, packet):
        """Procesa cada paquete capturado"""
        if IP in packet:
            info = {
                'src': packet[IP].src,
                'dst': packet[IP].dst,
                'protocol': 'TCP' if TCP in packet else 'UDP' if UDP in packet else 'IP',
                'size': len(packet)
            }
            self.packets.append(info)
            print(f"[+] {info['src']} -> {info['dst']} ({info['protocol']})")
    
    def start_capture(self, count=10):
        """Inicia captura de paquetes"""
        print(f"[*] Capturando {count} paquetes en {self.os_type}...")
        sniff(prn=self.packet_callback, count=count, iface=self.interface)
        return self.packets
