import random
import string
import hashlib

class PasswordGenerator:
    def __init__(self):
        self.lowercase_letters = string.ascii_lowercase
        self.uppercase_letters = string.ascii_uppercase
        self.digits = string.digits
        self.special_characters = string.punctuation

    def generate_password(self, length, use_lowercase=True, use_uppercase=True, use_digits=True, use_special=True):
        characters = ""
        if use_lowercase:
            characters += self.lowercase_letters
        if use_uppercase:
            characters += self.uppercase_letters
        if use_digits:
            characters += self.digits
        if use_special:
            characters += self.special_characters

        if not characters:
            print("Debe seleccionar al menos un tipo de caracteres.")
            return None

        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def hash_password(self, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

# Ejemplo de uso
if __name__ == "__main__":
    password_generator = PasswordGenerator()
    length = int(input("Longitud de la contraseña: "))

    use_lowercase = input("Incluir letras minúsculas (s/n): ").lower() == "s"
    use_uppercase = input("Incluir letras mayúsculas (s/n): ").lower() == "s"
    use_digits = input("Incluir números (s/n): ").lower() == "s"
    use_special = input("Incluir caracteres especiales (s/n): ").lower() == "s"

    password = password_generator.generate_password(length, use_lowercase, use_uppercase, use_digits, use_special)
    
    if password:
        print("Contraseña generada:", password)

        hash_option = input("¿Desea hashear la contraseña? (s/n): ").lower()
        if hash_option == "s":
            hashed_password = password_generator.hash_password(password)
            print("Contraseña hasheada:", hashed_password)
