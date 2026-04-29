"""Detección de anomalías con IA (modelo simple)"""
import random

class AnomalyDetector:
    def __init__(self):
        # Modelo simple basado en reglas + score
        self.baseline = {'normal_rate': 10, 'alert_threshold': 0.7}
    
    def analyze_traffic(self, packets):
        """Analiza paquetes y detecta anomalías"""
        alerts = []
        
        # Detectar posibles scans (muchos puertos desde misma IP)
        ip_requests = {}
        for p in packets:
            src = p['src']
            ip_requests[src] = ip_requests.get(src, 0) + 1
        
        for ip, count in ip_requests.items():
            if count > 5:  # Más de 5 paquetes = posible scan
                alerts.append({
                    'type': 'possible_port_scan',
                    'source': ip,
                    'severity': 'HIGH',
                    'packets_count': count
                })
        
        return {
            'total_packets': len(packets),
            'anomalies_detected': len(alerts),
            'alerts': alerts,
            'threat_score': min(1.0, len(alerts) / 10)
        }
