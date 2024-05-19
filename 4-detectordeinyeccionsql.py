import requests
from bs4 import BeautifulSoup

def sql_injection_detector(url):
    """
    Esta función intenta detectar vulnerabilidades de inyección SQL en una URL proporcionada.
    """
    # Intenta inyectar SQL en los parámetros de la URL
    injection_test_url = url + "'"
    response = requests.get(injection_test_url)

    # Si la respuesta contiene ciertos términos, es posible que la página sea vulnerable a la inyección SQL
    error_terms = ['mysql_fetch', 'syntax error', 'mysql_num_rows', 'mysql_fetch_array', 'Error Occurred While Processing Request', 'Server Error in', 'Microsoft OLE DB Provider for', 'error in your SQL syntax', 'Invalid Querystring', 'OLE DB Provider for ODBC', 'VBScript Runtime', 'ADODB.Field', 'BOF or EOF', 'ADODB.Command', 'JET Database', 'mysql_fetch_row', 'Syntax error', 'mysql_fetch_assoc', 'mysql_fetch_object', 'mysql_numrows', 'GetArray()', 'FetchRow()', 'Input string was not in a correct format']
    if any(term in response.text for term in error_terms):
        print(f'La URL {url} puede ser vulnerable a la inyección SQL.')

# Ejemplo de uso:
sql_injection_detector('http://example.com')
