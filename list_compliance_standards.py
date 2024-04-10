import requests
import logging
from authenticate_cspm import authenticate

def list_compliance_standards(auth_url, api_url, username, password):
    try:
        # Obtener el token de autenticación
        token = authenticate(auth_url, username, password)

        # URL del endpoint para listar los estándares de cumplimiento
        url = api_url

        # Headers con el token de autenticación
        headers = {
            'Accept': 'application/json; charset=UTF-8',
            'x-redlock-auth': token
        }

        # Realizar la solicitud GET para obtener los estándares de cumplimiento
        response = requests.request("GET", url, headers=headers)

        # Retornar la respuesta
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Error during API request: {e}")
        return None
