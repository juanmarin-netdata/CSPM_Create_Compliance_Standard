import logging
import config
from check_compliance_standard import check_and_create_compliance_standard
from list_compliance_standards import list_compliance_standards

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

# Llamar a la función para verificar y crear un estándar de cumplimiento
STANDARD_NAME = config.STANDARD_NAME
STANDARD_DESCRIPTION = config.STANDARD_DESCRIPTION
standard_id = check_and_create_compliance_standard(STANDARD_NAME, STANDARD_DESCRIPTION)

if standard_id:
    logging.info(f"ID del estándar de cumplimiento '{STANDARD_NAME}': {standard_id}")

# Consultar el listado de estándares de cumplimiento y obtener el ID del estándar creado
standards = list_compliance_standards(config.AUTH_URL, config.LIST_COMPLIANCE_STANDARD_URL, config.USERNAME, config.PASSWORD)

for standard in standards:
    if standard['name'] == STANDARD_NAME:
        logging.info(f"ID del estándar de cumplimiento '{STANDARD_NAME}' obtenido del listado: {standard['id']}")
