import socket
import struct

# Función para analizar paquetes y detectar intrusiones
def analyze_packet(packet):
    # Analizar la cabecera IP
    ip_header = packet[0:20]
    iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
    src_ip = socket.inet_ntoa(iph[8])
    dst_ip = socket.inet_ntoa(iph[9])
    print(f"Paquete desde {src_ip} hacia {dst_ip}")

    # Reglas simples de detección de intrusos
    if src_ip == "192.168.1.100":
        print(f"[ALERTA] Intruso detectado desde {src_ip}")

# Función principal para capturar y analizar paquetes
def ids():
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    sniffer.bind(("0.0.0.0", 0))
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    print("IDS básico en ejecución...")

    try:
        while True:
            packet, _ = sniffer.recvfrom(65565)
            analyze_packet(packet)
    except KeyboardInterrupt:
        print("IDS detenido.")
    finally:
        sniffer.close()

if __name__ == "__main__":
    ids()
