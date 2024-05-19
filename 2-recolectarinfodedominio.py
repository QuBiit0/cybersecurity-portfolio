import whois

# Función para recolectar información WHOIS de un dominio
def get_whois_info(domain):
    try:
        # Obtener la información WHOIS del dominio
        w = whois.whois(domain)
        print(f"Información WHOIS para {domain}:")
        print(f"Nombre del dominio: {w.domain_name}")
        print(f"Registrador: {w.registrar}")
        print(f"Fecha de creación: {w.creation_date}")
        print(f"Fecha de expiración: {w.expiration_date}")
        print(f"Servidores de nombres: {w.name_servers}")
    except Exception as e:
        print(f"Error al obtener información WHOIS para {domain}: {e}")

if __name__ == "__main__":
    # Dominio objetivo
    target_domain = "example.com"
    get_whois_info(target_domain)
