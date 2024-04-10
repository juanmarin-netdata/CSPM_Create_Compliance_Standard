import logging
import config
from list_compliance_standards import list_compliance_standards

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

AUTH_URL = config.AUTH_URL
USERNAME = config.USERNAME
PASSWORD = config.PASSWORD
LIST_COMPLIANCE_STANDARD_URL = config.LIST_COMPLIANCE_STANDARD_URL

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
