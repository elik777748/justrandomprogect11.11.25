def rp(a: list):
    if len(a) == len(set(a)):
        return True
    else:
        return False

if rp(list(input("Введіть свій ліст(int,str,float,bool): ").split(","))):
    print("Немае повторів")
else:
    print("Е повтори!")

