import logging
import config
from list_compliance_standards import list_compliance_standards
from add_compliance_standard import add_compliance_standard

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

AUTH_URL = config.AUTH_URL
USERNAME = config.USERNAME
PASSWORD = config.PASSWORD
LIST_COMPLIANCE_STANDARD_URL = config.LIST_COMPLIANCE_STANDARD_URL
STANDARD_NAME = config.STANDARD_NAME
STANDARD_DESCRIPTION = config.STANDARD_DESCRIPTION
ADD_COMPLIANCE_STANDARD_URL = config.ADD_COMPLIANCE_STANDARD_URL

# Ejecutar la función para listar los estándares de cumplimiento
try:
    standards = list_compliance_standards(AUTH_URL, LIST_COMPLIANCE_STANDARD_URL, USERNAME, PASSWORD)

    # Imprimir los estándares de cumplimiento si se obtuvieron correctamente
    if standards:
        logging.info("Estándares de cumplimiento:")
        for standard in standards:
            logging.info(standard)
except Exception as e:
    logging.error(f"Error durante la ejecución: {e}")

# Ejemplo de uso de la función para agregar un estándar de cumplimiento
try:
    # Agregar un estándar de cumplimiento
    response = add_compliance_standard(AUTH_URL, ADD_COMPLIANCE_STANDARD_URL, USERNAME, PASSWORD, STANDARD_NAME, STANDARD_DESCRIPTION)
    # Imprimir la respuesta
    if response:
        logging.info("Estándar de cumplimiento agregado:")
        logging.info(response)
except Exception as e:
    logging.error(f"Error durante la solicitud: {e}")
