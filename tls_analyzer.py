import scapy.all as scapy

def analyze_ssl_tls_traffic(interface):
    try:
        print(f"Iniciando el análisis de tráfico SSL/TLS en la interfaz {interface}...")
        # Filtra paquetes SSL/TLS
        packets = scapy.sniff(iface=interface, filter="port 443 or port 8443", count=10)
        
        for packet in packets:
            if packet.haslayer(scapy.TCP) and packet.haslayer(scapy.TLS):
                src_ip = packet[scapy.IP].src
                src_port = packet[scapy.TCP].sport
                dst_ip = packet[scapy.IP].dst
                dst_port = packet[scapy.TCP].dport
                
                print(f"Paquete SSL/TLS detectado: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")
                # Aquí puedes agregar más análisis o registro de datos según tus necesidades
                
    except KeyboardInterrupt:
        print("Análisis de tráfico SSL/TLS detenido por el usuario.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    interface = input("Ingrese el nombre de la interfaz de red a monitorear (por ejemplo, eth0): ")
    analyze_ssl_tls_traffic(interface)
