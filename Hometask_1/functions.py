def check_duplicates(a: list):
    """Перевіряє, чи містить список дублікати"""
    if len(a) == len(set(a)):
        return True
    else:
        return False


def check_password(a: str):
    """Ця функція перевіряє пароль на параметри такі як: Довжина(більше 8 символів), Цифра(наявність хоча б однією цифри), Caps(наявність великої та маленької букви)"""
    d = False
    s = False
    r = False
    if len(a) >= 8:
        for g in a:
            if g.isdigit():
                d = True
            if g.isupper():
                s = True
            if g.islower():
                r = True
    if d == True and s == True and r == True:
        return True
    else:
        return False
        

def check_temperature(temperature: int):
    """Перевіряє значення. Якщо більше ніж 20, то поверне True інакше False"""
    if temperature <= 20:
        return False
    else:
        return True

