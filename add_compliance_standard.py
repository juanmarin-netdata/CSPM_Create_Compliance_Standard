import requests
import json
import logging
from authenticate_cspm import authenticate

def add_compliance_standard(auth_url, api_url, username, password, name, description):
    try:
        # Obtener el token de autenticación
        token = authenticate(auth_url, username, password)

        # Cuerpo de la solicitud para agregar un estándar de cumplimiento
        payload = json.dumps({
            "description": description,
            "name": name
        })

        # Headers con el token de autenticación y el tipo de contenido
        headers = {
            'Content-Type': 'application/json',
            'x-redlock-auth': token
        }

        # Realizar la solicitud POST para agregar un estándar de cumplimiento
        response = requests.post(api_url, headers=headers, data=payload)

        # Si la respuesta está vacía, se asume que la operación fue exitosa
        if not response.text:
            logging.info(f"Compliance Standard '{name}' creado exitosamente.")
            return None
        else:
            # Retornar la respuesta
            return response.json()
    except requests.RequestException as e:
        logging.error(f"Error durante la solicitud: {e}")
        return None


