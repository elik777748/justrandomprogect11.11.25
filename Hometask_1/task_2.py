def check_duplicates(a: list):
    """Перевіряє, чи містить список дублікати"""
    if len(a) == len(set(a)):
        return True
    else:
        return False

if check_duplicates(list(input("Введіть свій ліст(int,str,float,bool): ").split(","))):
    print("Немае повторів")
else:
    print("Е повтори!")

