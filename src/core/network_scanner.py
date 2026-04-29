"""Escáner inteligente de red"""
import subprocess
import platform
import ipaddress
import concurrent.futures
from typing import List, Dict

class NetworkScanner:
    def __init__(self):
        self.os_type = platform.system()
        
    def ping_host(self, ip: str) -> Dict:
        """Ping a un host"""
        param = '-n' if self.os_type == 'Windows' else '-c'
        command = ['ping', param, '1', ip]
        
        try:
            result = subprocess.run(command, capture_output=True, timeout=2)
            return {
                'ip': ip,
                'alive': result.returncode == 0,
                'response_time': None  # Se puede extraer del output
            }
        except:
            return {'ip': ip, 'alive': False}
    
    def scan_network(self, network: str, max_workers=20) -> List[Dict]:
        """Escanea red completa con hilos"""
        try:
            net = ipaddress.ip_network(network, strict=False)
            ips = [str(ip) for ip in net.hosts()][:254]  # Limitar a /24
            
            print(f"[*] Escaneando {len(ips)} hosts en {network}")
            
            results = []
            with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
                future_to_ip = {executor.submit(self.ping_host, ip): ip for ip in ips}
                
                for future in concurrent.futures.as_completed(future_to_ip):
                    result = future.result()
                    if result['alive']:
                        results.append(result)
                        print(f"[+] Host encontrado: {result['ip']}")
            
            return results
            
        except Exception as e:
            print(f"[-] Error en escaneo: {e}")
            return []
    
    def intelligent_scan(self, network: str):
        """Escaneo inteligente con priorización"""
        print("[*] Iniciando escaneo inteligente...")
        
        # Primero escanear IPs comunes
        common_ips = ['.1', '.254', '.100', '.200']
        base_ip = network.rsplit('.', 1)[0]
        
        priority_hosts = []
        for suffix in common_ips:
            priority_hosts.append(f"{base_ip}{suffix}")
        
        print("[*] Escaneando hosts prioritarios...")
        for ip in priority_hosts:
            result = self.ping_host(ip)
            if result['alive']:
                print(f"[!] Host prioritario activo: {ip}")
        
        # Luego escanear el resto
        return self.scan_network(network)
