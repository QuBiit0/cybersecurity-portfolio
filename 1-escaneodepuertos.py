import socket

def port_scanner(host, port):
    """
    Esta función intenta establecer una conexión con el host y el puerto especificados.
    Si la conexión es exitosa, el puerto está abierto. De lo contrario, está cerrado.
    """
    try:
        socket.create_connection((host, port))
        return True
    except OSError:
        return False

# Ejemplo de uso:
for port in range(1, 1024):
    if port_scanner('localhost', port):
        print(f'El puerto {port} está abierto.')
    else:
        print(f'El puerto {port} está cerrado.')
