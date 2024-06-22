import re

def verificar_password(password):
    # Casos específicos
    if len(password) > 10:
        return "Supera 10 caracteres"
    if len(password) < 8:
        return "Menor a 8 caracteres"
    
    # Condiciones generales
    tiene_mayuscula = re.search(r'[A-Z]', password) is not None
    tiene_minuscula = re.search(r'[a-z]', password) is not None
    tiene_numero = re.search(r'[0-9]', password) is not None
    tiene_especial = re.search(r'[\W_]', password) is not None
    
    if not tiene_mayuscula:
        return "No tiene letra mayúscula"
    if not tiene_minuscula:
        return "No tiene letra minúscula"
    if not any(char.isalpha() for char in password):
        return "No tiene letras"
    if not tiene_numero:
        return "No tiene número"
    if not tiene_especial:
        return "No tiene carácter especial"
    
    if 8 <= len(password) <= 10:
        return "Cumple todas las condiciones"

# Ejemplos de uso
passwords = [
    "Pass123!",
    "12345678",
    "password",
    "PASSWORD",
    "PassWord1",
    "Pass12345678!",
    "P@ssw0rd",
    "Short1!"
]

for pwd in passwords:
    print(f"Password: {pwd} - {verificar_password(pwd)}")
