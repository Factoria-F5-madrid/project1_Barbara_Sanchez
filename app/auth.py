import json
import os
from getpass import getpass

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
USERS_FILE = os.path.join(DATA_DIR, "users.json")

def load_users(file_path=USERS_FILE):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            original_users = json.load(f)
            return {k.lower(): v for k, v in original_users.items()}
    except FileNotFoundError:
        print("Archivo de usuarios no encontrado.")
        return {}

def authenticate():
    users = load_users()
    username = input("Usuario: ").strip().lower()
    password = getpass("Contraseña: ")
    print("-" * 20)

    if username in users and users[username] == password:
        return True
    else:
        print("Usuario o contraseña incorrectos")
        return False
