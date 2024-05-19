import socket
import threading

# Función para escanear un puerto específico
def scan_port(ip, port):
    try:
        # Crear un socket para la conexión
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Puerto {port} está abierto.")
        sock.close()
    except Exception as e:
        print(f"Error al escanear el puerto {port}: {e}")

# Función principal para escanear un rango de puertos
def port_scanner(ip, start_port, end_port):
    print(f"Escaneando {ip} desde el puerto {start_port} hasta el puerto {end_port}...")
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port))
        thread.start()

if __name__ == "__main__":
    # Dirección IP y rango de puertos a escanear
    target_ip = "192.168.1.1"
    start_port = 1
    end_port = 1024
    port_scanner(target_ip, start_port, end_port)
