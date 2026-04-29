# Agregar al principio
from ai.advanced_ai import AdvancedNetworkAI
from core.network_scanner import NetworkScanner

# Agregar nuevos comandos en la función main()

elif sys.argv[1] == 'predict':
    print("[*] Prediciendo uso de ancho de banda...")
    ai = AdvancedNetworkAI()
    
    # Simular datos históricos
    historical = np.random.normal(100, 20, 24).tolist()
    prediction = ai.predict_bandwidth_usage(historical)
    
    print(f"📈 Predicción para próxima hora: {prediction['next_hour']} MB/s")
    print(f"   Confianza: {prediction['confidence']*100}%")
    print(f"   Tendencia: {prediction['trend']}")

elif sys.argv[1] == 'scan':
    target = '192.168.1.0/24'
    if '--target' in sys.argv:
        idx = sys.argv.index('--target')
        if idx + 1 < len(sys.argv):
            target = sys.argv[idx + 1]
    
    scanner = NetworkScanner()
    results = scanner.intelligent_scan(target)
    
    print(f"\n✓ Escaneo completado. Hosts encontrados: {len(results)}")
    for host in results:
        print(f"  • {host['ip']}")

elif sys.argv[1] == 'recommend':
    print("[*] Generando recomendaciones de seguridad...")
    
    # Simular amenazas detectadas
    sample_threats = [
        {'type': 'possible_port_scan', 'source': '192.168.1.100'},
        {'type': 'bruteforce', 'source': '10.0.0.50'}
    ]
    
    ai = AdvancedNetworkAI()
    rules = ai.recommend_firewall_rules(sample_threats)
    
    print("\n🛡️ REGLAS DE FIREWALL RECOMENDADAS:")
    for rule in rules:
        print(f"\n  • {rule['reason']}")
        print(f"    → Linux: {rule['command_linux'][:60]}...")
        print(f"    → Windows: {rule['command_windows']}")
