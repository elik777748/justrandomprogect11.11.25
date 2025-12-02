from functions import is_valid_password, is_temperature_above_20, has_duplicates

if is_temperature_above_20(18):
    print("тепло")
else:
    print("холодно")

if has_duplicates(list(input("Введіть свій список(int,str,float,bool): ").split(","))):
    print("Немає повторів")
else:
    print("Е повтори!")


while True:
    if is_valid_password(input("Введіть пароль: ")) == True:
        print("Password strong")
        break
    else: 
        print("Password bad")

    