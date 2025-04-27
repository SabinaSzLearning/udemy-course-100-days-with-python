import requests
from datetime import datetime

MY_LAT = 50.0647 # Your latitude
MY_LONG = 19.9450 # Your longitude


def check_ISS_position(lat, lng):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if lat-5 < iss_latitude < lat+5 and lng-5 < iss_longitude < lng+5:
        return True
    return False


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if sunset < time_now.hour or time_now.hour < sunrise:
        return True
    return False



if check_ISS_position(MY_LAT, MY_LONG) and is_dark():
    print("ISS is in the sky")







