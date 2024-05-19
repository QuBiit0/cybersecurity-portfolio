import socket
import ipaddress

def network_scanner(network):
    """
    Esta función escanea una red en busca de hosts activos.
    """
    for ip in ipaddress.IPv4Network(network):
        try:
            socket.gethostbyaddr(str(ip))
            print(f'El host {ip} está activo.')
        except socket.herror:
            pass

# Ejemplo de uso:
network_scanner('192.168.1.0/24')
