"""Modelos de IA avanzados para análisis de red"""
import numpy as np
import json
from collections import defaultdict
from datetime import datetime, timedelta

class AdvancedNetworkAI:
    def __init__(self):
        self.traffic_history = []
        self.attack_patterns = self.load_attack_patterns()
        
    def load_attack_patterns(self):
        """Patrones conocidos de ataques"""
        return {
            'ddos': {'rate': 100, 'same_ip': True},
            'bruteforce': {'port': 22, 'attempts': 10},
            'syn_flood': {'tcp_flags': 'SYN', 'rate': 50},
            'dns_amplification': {'port': 53, 'size': 1000}
        }
    
    def predict_bandwidth_usage(self, historical_data):
        """Predice uso de ancho de banda con regresión simple"""
        if len(historical_data) < 2:
            return {'prediction': 'insufficient_data', 'next_hour': 0}
        
        # Media móvil simple
        window_size = min(10, len(historical_data))
        recent = historical_data[-window_size:]
        prediction = np.mean(recent) * 1.1  # +10% tendencia
        
        return {
            'prediction': 'stable',
            'next_hour': round(prediction, 2),
            'confidence': 0.75,
            'trend': 'increasing' if recent[-1] > recent[0] else 'decreasing'
        }
    
    def detect_zero_day_anomaly(self, packets):
        """Detección de anomalías con isolation forest (simulado)"""
        features = []
        for p in packets:
            feature_vector = [
                len(p.get('src', '')),  # longitud IP
                p.get('size', 0),
                1 if p.get('protocol') == 'TCP' else 0,
                1 if p.get('protocol') == 'UDP' else 0
            ]
            features.append(feature_vector)
        
        # Versión simplificada de isolation forest
        scores = []
        for f in features:
            # Puntaje de anomalía basado en desviación
            anomaly_score = np.random.normal(0.1, 0.05)  # Simulado
            scores.append(anomaly_score)
        
        anomalies = [i for i, score in enumerate(scores) if score > 0.15]
        
        return {
            'anomaly_indices': anomalies,
            'anomaly_ratio': len(anomalies) / len(packets) if packets else 0,
            'suspicious_ips': list(set([packets[i]['src'] for i in anomalies if i < len(packets)]))
        }
    
    def recommend_firewall_rules(self, detected_threats):
        """Genera reglas de firewall recomendadas"""
        rules = []
        
        for threat in detected_threats:
            if threat['type'] == 'possible_port_scan':
                rules.append({
                    'action': 'block',
                    'source': threat['source'],
                    'reason': 'Port scan detected',
                    'command_linux': f"sudo iptables -A INPUT -s {threat['source']} -j DROP",
                    'command_windows': f"netsh advfirewall firewall add rule name='Block {threat['source']}' dir=in action=block remoteip={threat['source']}"
                })
            elif threat['type'] == 'bruteforce':
                rules.append({
                    'action': 'rate_limit',
                    'port': 22,
                    'reason': 'SSH bruteforce attempt',
                    'command_linux': "sudo iptables -A INPUT -p tcp --dport 22 -m limit --limit 3/min -j ACCEPT"
                })
        
        return rules
