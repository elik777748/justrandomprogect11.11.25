from functions import check_password, check_duplicates, check_temperature

if check_temperature(18):
    print("тепло")
else:
    print("холодно")

if check_duplicates(list(input("Введіть свій список(int,str,float,bool): ").split(","))):
    print("Немає повторів")
else:
    print("Е повтори!")


while True:
    if check_password(input("Введіть пароль: ")) == True:
        print("Password strong")
        break
    else: 
        print("Password bad")

    