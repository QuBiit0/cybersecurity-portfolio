import requests

def web_security_audit(url):
    """
    Esta función realiza una auditoría de seguridad básica en una aplicación web.
    """
    response = requests.get(url)
    if 'X-Content-Type-Options' not in response.headers:
        print(f'La URL {url} podría ser vulnerable a los ataques MIME Sniffing.')
    if 'X-XSS-Protection' not in response.headers:
        print(f'La URL {url} podría ser vulnerable a los ataques XSS.')
    if 'Content-Security-Policy' not in response.headers:
        print(f'La URL {url} podría ser vulnerable a varios tipos de ataques.')

# Ejemplo de uso:
web_security_audit('http://example.com')
