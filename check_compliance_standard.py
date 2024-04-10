import logging
import config
from list_compliance_standards import list_compliance_standards
from add_compliance_standard import add_compliance_standard

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def check_and_create_compliance_standard(name, description):
    try:
        standards = list_compliance_standards(config.AUTH_URL, config.LIST_COMPLIANCE_STANDARD_URL, config.USERNAME, config.PASSWORD)

        # Verificar si ya existe un estándar con el nombre dado
        for standard in standards:
            if standard['name'] == name:
                logging.info(f"El estándar de cumplimiento '{name}' ya existe. No es necesario crear uno nuevo.")
                return standard['id']  # Devolver el ID del estándar existente

        # Si no existe, agregar un estándar de cumplimiento nuevo
        add_compliance_standard(config.AUTH_URL, config.ADD_COMPLIANCE_STANDARD_URL, config.USERNAME, config.PASSWORD, name, description)
        logging.info(f"Estándar de cumplimiento '{name}' creado exitosamente.")
        return None
    except Exception as e:
        logging.error(f"Error durante la ejecución: {e}")
        return None
