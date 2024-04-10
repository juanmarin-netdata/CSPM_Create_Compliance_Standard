import requests
import logging

def authenticate(url, username, password):
    try:
        data_login = {"username": username, "password": password}
        response = requests.post(url, json=data_login)
        response.raise_for_status()
        return response.json()['token']
    except requests.RequestException as e:
        logging.error(f"Error during authentication: {e}")
        exit(1)
