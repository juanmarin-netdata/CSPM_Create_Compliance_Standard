import pandas as pd
import requests
import logging
import json
from authenticate_cspm import authenticate

def add_compliance_requirement(auth_url, prisma_url, username, password, compliance_id):
    try:
        # Obtener el token de autenticación
        token = authenticate(auth_url, username, password)

        # Leer el archivo excel
        df = pd.read_excel('compliance_standard.xlsx')

        # Crear un conjunto para almacenar los nombres de requisitos únicos
        unique_requirements = set()

        # Iterar sobre las filas del DataFrame y agregar los nombres únicos al conjunto
        for index, row in df.iterrows():
            unique_requirements.add(row['Compliance Requirement'])

        # Iterar sobre los nombres únicos y crear los requisitos de cumplimiento
        for name in unique_requirements:
            # Obtener la descripción y el ID del requisito
            description = df.loc[df['Compliance Requirement'] == name, 'Description'].iloc[0]
            requirement_id = df.loc[df['Compliance Requirement'] == name, 'Requirement ID'].iloc[0]

            # URL del endpoint para agregar un requisito de cumplimiento
            url = f"{prisma_url}/compliance/{compliance_id}/requirement"

            # Payload para la solicitud POST
            payload = json.dumps({
                "description": description,
                "name": name,
                "requirementId": requirement_id
            })

            # Headers con el token de autenticación
            headers = {
                'Content-Type': 'application/json',
                'x-redlock-auth': token
            }

            # Realizar la solicitud POST para agregar el requisito de cumplimiento
            response = requests.post(url, headers=headers, data=payload)

            # Verificar si la solicitud fue exitosa
            if response.status_code == 200:
                logging.info(f"Requisito de cumplimiento '{name}' creado exitosamente.")
            else:
                logging.error(f"Error al crear el requisito de cumplimiento '{name}': El Requeriment ID ya existe")

    except Exception as e:
        logging.error(f"Error durante la ejecución: {e}")
