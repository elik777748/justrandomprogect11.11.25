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
        

while True:
    if check_password(input("Введіть пароль: ")) == True:
        print("Password strong")
        break
    else: 
        print("Pasword bad")

    

    