import requests
def temperature(city: str):
    temperature = ""
    url = f"https://wttr.in/{city}?format=%t" 
    try:
        response = requests.get(url)
        response.raise_for_status()
        for i in response.text:
            if i.isdigit():
                temperature += i
        return temperature
    except Exception as e:
        return "ERROR"

print(f"Зараз у місті {temperature("Odesa")} градусів")
#Якщо не спрацівало спробуйте ще раз
