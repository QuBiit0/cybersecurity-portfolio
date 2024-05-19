import socket

# Función para analizar paquetes capturados
def analyze_packet(packet):
    print(f"Paquete capturado: {packet}")

# Función principal para capturar paquetes de red
def network_sniffer():
    # Crear un socket para capturar paquetes de red
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    # Asignar una dirección IP y puerto al socket
    sniffer.bind(("0.0.0.0", 0))
    # Incluir la cabecera IP en el paquete
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    print("Sniffer de red en ejecución...")

    try:
        while True:
            # Capturar un paquete
            packet, _ = sniffer.recvfrom(65565)
            # Analizar el paquete capturado
            analyze_packet(packet)
    except KeyboardInterrupt:
        print("Sniffer de red detenido.")
    finally:
        sniffer.close()

if __name__ == "__main__":
    network_sniffer()
