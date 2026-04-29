"""CLI principal de Networking AI"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.packet_capture import PacketCapture
from ai.detector import AnomalyDetector

def main():
    print("""
    ╔══════════════════════════════════╗
    ║     Networking AI v0.1           ║
    ║     Herramienta de Red con IA    ║
    ╚══════════════════════════════════╝
    """)
    
    if len(sys.argv) < 2:
        print("Uso: python main.py <comando>")
        print("\nComandos disponibles:")
        print("  monitor --packets N   - Captura y analiza N paquetes")
        print("  scan --target IP      - Escanea red (beta)")
        print("  help                  - Muestra ayuda")
        return
    
    if sys.argv[1] == 'monitor':
        packets_count = 10
        if '--packets' in sys.argv:
            idx = sys.argv.index('--packets')
            if idx + 1 < len(sys.argv):
                packets_count = int(sys.argv[idx + 1])
        
        # Capturar paquetes
        capture = PacketCapture()
        packets = capture.start_capture(count=packets_count)
        
        # Analizar con IA
        detector = AnomalyDetector()
        result = detector.analyze_traffic(packets)
        
        # Mostrar resultados
        print("\n📊 RESULTADOS DEL ANÁLISIS:")
        print(f"   Paquetes analizados: {result['total_packets']}")
        print(f"   Anomalías detectadas: {result['anomalies_detected']}")
        print(f"   Threat Score: {result['threat_score']*100}%")
        
        if result['alerts']:
            print("\n⚠️ ALERTAS:")
            for alert in result['alerts']:
                print(f"   • {alert['type']} desde {alert['source']} (severidad: {alert['severity']})")
        else:
            print("\n✅ Tráfico normal - No se detectaron anomalías")
    
    elif sys.argv[1] == 'help':
        print("Networking AI - Comandos:")
        print("  monitor --packets 20   - Analiza 20 paquetes")
        print("  scan --target 192.168.1.1 - Escanea IP específica")
    
    else:
        print(f"❌ Comando desconocido: {sys.argv[1]}")

if __name__ == "__main__":
    main()
