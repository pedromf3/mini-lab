import secrets
import string

alphabet = string.ascii_lowercase
symbols = "!*%$&?-_.:#@"
digits = string.digits

def generate_password(length):
    if length <= 0:
        raise ValueError("Password length must be greater than 0.")
    
    all_characters = alphabet + alphabet.upper() + digits + symbols
    return ''.join(secrets.choice(all_characters) for _ in range(length))
