import re

# Función para analizar un archivo de logs y detectar intentos de intrusión
def analyze_logs(log_file):
    # Expresión regular para detectar intentos de inicio de sesión fallidos
    pattern = re.compile(r"Failed password for (invalid user )?(?P<username>\w+) from (?P<ip>\d+\.\d+\.\d+\.\d+)")
    intrusions = {}

    with open(log_file, "r") as file:
        for line in file:
            match = pattern.search(line)
            if match:
                ip = match.group("ip")
                intrusions[ip] = intrusions.get(ip, 0) + 1

    for ip, count in intrusions.items():
        print(f"{count} intentos fallidos desde {ip}")

if __name__ == "__main__":
    # Archivo de logs objetivo
    log_file_path = "/var/log/auth.log"
    analyze_logs(log_file_path)
