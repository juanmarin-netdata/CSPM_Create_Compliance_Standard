import requests
import logging
from authenticate_cspm import authenticate


def list_compliance_requirements(auth_url, PRISMA_URL, username, password, compliance_id):
    try:
        # Obtener el token de autenticación
        token = authenticate(auth_url, username, password)

        # URL del endpoint para listar los requisitos de cumplimiento
        url = f"{PRISMA_URL}/compliance/{compliance_id}/requirement"

        # Headers con el token de autenticación
        headers = {
            'Accept': '*/*',
            'x-redlock-auth': token
        }

        # Realizar la solicitud GET para obtener los requisitos de cumplimiento
        response = requests.request("GET", url, headers=headers)

        # Verificar si la respuesta es exitosa
        if response.status_code == 200:
            print(response.json())
        else:
            logging.error(f"Error durante la solicitud: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        logging.error(f"Error durante API request: {e}")


