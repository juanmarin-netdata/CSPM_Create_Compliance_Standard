import logging
import config
from check_compliance_standard import check_and_create_compliance_standard
from list_compliance_standards import list_compliance_standards
from add_compliance_requirement import add_compliance_requirement
from list_compliance_requirements import list_compliance_requirements
from add_compliance_section import create_compliance_sections_from_dict
import pandas as pd

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
        compliance_id = standard['id']
        logging.info(f"ID del estándar de cumplimiento '{STANDARD_NAME}' obtenido del listado: {compliance_id}")
        break

# Crear los requisitos de cumplimiento
add_compliance_requirement(config.AUTH_URL, config.PRISMA_URL, config.USERNAME, config.PASSWORD, compliance_id)

# Obtener los requerimientos
requirements_dict = list_compliance_requirements(config.AUTH_URL, config.PRISMA_URL, config.USERNAME, config.PASSWORD, compliance_id)
logging.info(requirements_dict)

# Crear las secciones de cumplimiento desde un diccionario
create_compliance_sections_from_dict(config.AUTH_URL, config.PRISMA_URL, config.USERNAME, config.PASSWORD, requirements_dict)
