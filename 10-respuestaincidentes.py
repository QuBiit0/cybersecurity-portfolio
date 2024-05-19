import os

def incident_response(incident_type):
    """
    Esta función realiza una respuesta básica a un incidente de seguridad.
    """
    if incident_type == 'malware':
        os.system('clamscan -r --remove /')
    elif incident_type == 'unauthorized_access':
        os.system('last')
    else:
        print('Tipo de incidente no reconocido.')

# Ejemplo de uso:
incident_response('malware')
