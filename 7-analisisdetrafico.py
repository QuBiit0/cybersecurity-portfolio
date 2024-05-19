from scapy.all import *

def packet_analysis(packet):
    """
    Esta función analiza un paquete de red y muestra su información.
    """
    print(packet.summary())

# Ejemplo de uso:
sniff(prn=packet_analysis, count=10)
