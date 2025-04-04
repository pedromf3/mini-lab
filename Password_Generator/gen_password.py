# Author: Pedro Ferreira
# Last Updated: April 4, 2025

import secrets
import argparse
import string

# Define character pools
alphabet = string.ascii_lowercase
symbols = "!*%$&?-_.:#@"
digits = string.digits

def generate_password(length):
    if length <= 0:
        raise ValueError("Password length must be greater than 0.")
    
    # Combine all character pools
    all_characters = alphabet + alphabet.upper() + digits + symbols
    
    # Generate a secure password
    password = ''.join(secrets.choice(all_characters) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description="Create a secure password.")
    parser.add_argument("length", help="The length of the password to be generated.", type=int)
    args = parser.parse_args()
    
    try:
        password = generate_password(args.length)
        print(password)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()