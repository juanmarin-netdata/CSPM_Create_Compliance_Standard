import requests
import json
import pandas as pd
import logging
from authenticate_cspm import authenticate

def add_compliance_section(auth_url, prisma_url, username, password, requirement_id, section_id):
    try:
        # Obtener el token de autenticación
        token = authenticate(auth_url, username, password)

        # URL del endpoint para agregar una sección de cumplimiento
        url = f"{prisma_url}/compliance/{requirement_id}/section"

        # Payload para la solicitud POST
        payload = json.dumps({
            "sectionId": section_id
        })

        # Headers con el token de autenticación
        headers = {
            'Content-Type': 'application/json',
            'x-redlock-auth': token
        }

        # Realizar la solicitud POST para agregar la sección de cumplimiento
        response = requests.post(url, headers=headers, data=payload)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            logging.info(f"Sección de cumplimiento '{section_id}' creada exitosamente para el requisito '{requirement_id}'.")
        else:
            logging.error(f"Error al crear la sección de cumplimiento '{section_id}' para el requisito '{requirement_id}': {response.status_code} - {response.text}")

    except Exception as e:
        logging.error(f"Error durante la ejecución: {e}")

def create_compliance_sections_from_dict(auth_url, prisma_url, username, password, requirement_dict):
    try:
        # Obtener el token de autenticación
        token = authenticate(auth_url, username, password)

        # Iterar sobre los elementos del dict
        for requirement_id, requirement_name in requirement_dict.items():
            # Leer el archivo excel
            excel_file = "compliance_standard.xlsx"
            df = pd.read_excel(excel_file)

            # Filtrar el DataFrame por el Requirement ID actual
            sections_df = df[df['Requirement ID'] == requirement_name]

            # Iterar sobre las secciones del Requirement ID actual
            for index, row in sections_df.iterrows():
                section_id = row['Section ID']

                # Crear la sección de cumplimiento
                add_compliance_section(auth_url, prisma_url, username, password, requirement_id, section_id)

    except Exception as e:
        logging.error(f"Error durante la ejecución: {e}")

