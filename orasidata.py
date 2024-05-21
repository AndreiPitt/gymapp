import datetime
import requests


def detaliidatatimp():
    now = datetime.datetime.now()
    ceas = now.strftime("%H:%M:%S")
    ziua_prescurtata = now.strftime("%a")  # Mon
    ziua_intreaga = now.strftime("%A")  # Monday
    ora_curenta = now.strftime("%H")  # 12
    ziua_curenta = now.strftime("%w")  # 1
    if ziua_curenta == "0":
        ziua_curenta = "7"
    tuplu = (ziua_prescurtata, ziua_intreaga, ora_curenta, ziua_curenta, ceas)
    return tuplu


def get_day_of_year():
    azi = datetime.date.today()
    ziua_curenta = azi.timetuple().tm_yday
    year = azi.year
    zile_din_an = 366 if (year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)) else 365
    tuplu = (ziua_curenta, zile_din_an)
    return tuplu


def returneaza_vremea():
    # Introdu aici cheia ta API obținută de la OpenWeatherMap
    api_key = "33521462be9a9eb3b7970c167d4e2003"
    city_name = "Timisoara"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Construieste URL-ul final
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"

    # Trimite cererea HTTP
    response = requests.get(complete_url)

    # Extrage datele în format JSON
    data = response.json()
    print(data)
    # Verifică dacă cererea a fost cu succes
    if data["cod"] != "404":
        main = data["main"]
        temperature = main["temp"]
        temperature = int(temperature)
        # print(f"Temperatura actuală în {city_name} este {temperature}°C")
        return str(temperature)
    else:
        print("Orașul nu a fost găsit!")
        return "Eroare"


print(returneaza_vremea())
