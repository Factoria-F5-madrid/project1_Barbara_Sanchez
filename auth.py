import json
from getpass import getpass

def load_users(file_path="users.json"):
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
