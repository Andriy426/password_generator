import random
import string

def generate_password(length=12, use_digits=True, use_special=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    print("Згенерований пароль:", generate_password(16))
    print("Короткий без спецсимволів:", generate_password(10, use_special=False))
