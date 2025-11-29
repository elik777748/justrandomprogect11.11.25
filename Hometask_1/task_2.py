def check_duplicates(a: list):
    """Перевіряє, чи містить список дублікати"""
    if len(a) == len(set(a)):
        return True
    else:
        return False

if check_duplicates(list(input("Введіть свій список(int,str,float,bool): ").split(","))):
    print("Немає повторів")
else:
    print("Е повтори!")

