def check_temperature(temperature: int):
    """Перевіряє значення. Якщо більше ніж 20, то поверне True інакше False"""
    if temperature <= 20:
        return False
    else:
        return True

if check_temperature(18):
    print("тепло")
else:
    print("холодно")
