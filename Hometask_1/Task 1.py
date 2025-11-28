def cp(a: str):
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
    if cp(input("Введіть пароль: ")) == True:
        print("Password strong")
        break
    else: 
        print("Pasword bad")

    

    