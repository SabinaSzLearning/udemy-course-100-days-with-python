import requests

LAT = 44.34
LONG = 10.99
APIkey = "3ef4410d37bbc06581971334848dc4b3"
url = "https://api.openweathermap.org/data/2.5/forecast"

weather_prams = {
    'lat': LAT,
    'lon': LONG,
    'cnt': 4,
    'appid': APIkey
}



response = requests.get(url=url, params=weather_prams)
response.raise_for_status()
data = response.json()


take_umbrela = False
for item in data['list']:
    for item2 in item['weather']:
        if item2['id'] < 700:
            take_umbrela = True
            print(item2['id'])

print(take_umbrela)
