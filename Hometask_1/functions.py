def check_duplicates(items: list):
    """Перевіряє, чи містить список дублікати"""
    if len(items) == len(set(items)):
        return True
    else:
        return False


def check_password(password: str):
    """Ця функція перевіряє пароль на параметри такі як: Довжина(більше 8 символів), Цифра(наявність хоча б однієї цифри), Caps(наявність великої та маленької букви)"""
    has_digit = False
    has_upper = False
    has_lower = False
    if len(password) >= 8:
        for char in password:
            if char.isdigit():
                has_digit = True
            if char.isupper():
                has_upper = True
            if char.islower():
                has_lower = True
    if has_digit and has_upper and has_lower:
        return True
    else:
        return False


def check_temperature(temp_celsius: int):
    """Перевіряє значення. Якщо більше ніж 20, то поверне True інакше False"""
    if temp_celsius <= 20:
        return False
    else:
        return True