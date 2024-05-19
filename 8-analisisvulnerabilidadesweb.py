import requests

# Función para escanear una URL en busca de vulnerabilidades comunes
def web_vulnerability_scanner(url):
    # Listado de patrones de vulnerabilidades comunes
    vulnerabilities = {
        "SQL Injection": "' OR '1'='1",
        "XSS": "<script>alert('XSS')</script>"
    }

    for vuln_name, payload in vulnerabilities.items():
        try:
            # Inyectar el payload en la URL
            vuln_url = f"{url}?q={payload}"
            response = requests.get(vuln_url)
            if payload in response.text:
                print(f"Vulnerabilidad {vuln_name} detectada en {vuln_url}")
            else:
                print(f"No vulnerable a {vuln_name} en {vuln_url}")
        except Exception as e:
            print(f"Error al probar {vuln_url}: {e}")

if __name__ == "__main__":
    # URL objetivo
    target_url = "http://example.com/search"
    web_vulnerability_scanner(target_url)
