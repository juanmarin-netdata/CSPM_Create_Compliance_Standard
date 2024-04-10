import logging
from authenticate_cspm import authenticate
import config

AUTH_URL = config.AUTH_URL
USERNAME = config.USERNAME
PASSWORD = config.PASSWORD

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

token = authenticate(AUTH_URL, USERNAME, PASSWORD)
logging.info(f"Token obtenido: {token}")
