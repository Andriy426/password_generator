# password_generator.py
"""
Генератор безпечних паролів з налаштуваннями через аргументи командного рядка.
"""

import random
import string
import argparse


def generate_password(
    length: int = 16,
    use_digits: bool = True,
    use_special: bool = True,
    use_upper: bool = True,
    use_lower: bool = True
) -> str:
    """
    Генерує пароль заданої довжини з вибраними групами символів.
    """
    if length < 4:
        raise ValueError("Довжина пароля має бути не менше 4 символів")

    chars = ""
    if use_lower:
        chars += string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?/~"

    if not chars:
        raise ValueError("Потрібно вибрати хоча б один тип символів")

    return ''.join(random.choice(chars) for _ in range(length))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Генератор безпечних паролів")
    parser.add_argument("-l", "--length", type=int, default=16, help="Довжина пароля (4–64)")
    parser.add_argument("--no-digits", action="store_false", dest="use_digits", help="Без цифр")
    parser.add_argument("--no-special", action="store_false", dest="use_special", help="Без спецсимволів")
    parser.add_argument("--no-upper", action="store_false", dest="use_upper", help="Без великих літер")
    parser.add_argument("--no-lower", action="store_false", dest="use_lower", help="Без малих літер")
    parser.add_argument("-c", "--count", type=int, default=1, help="Скільки паролів згенерувати")
    args = parser.parse_args()

    if not (4 <= args.length <= 64):
        print("Довжина має бути від 4 до 64. Використовую 16.")
        args.length = 16

    print("Згенеровані паролі:\n")
    for i in range(args.count):
        pw = generate_password(
            args.length,
            args.use_digits,
            args.use_special,
            args.use_upper,
            args.use_lower
        )
        print(f"{i+1:2d}. {pw}")
