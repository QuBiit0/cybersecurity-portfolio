from scapy.all import *

def intrusion_detection(packet):
    """
    Esta función detecta posibles intrusiones en la red.
    """
    if packet.haslayer(TCP) and packet[TCP].flags == 'S':
        print(f'Detección de posible escaneo de puertos desde {packet[IP].src} a {packet[IP].dst}.')

# Ejemplo de uso:
sniff(prn=intrusion_detection)
