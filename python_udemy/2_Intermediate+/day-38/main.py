import requests
from datetime import datetime
import os


## Data
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
TOKEN = os.environ.get("TOKEN")

URL = 'https://trackapi.nutritionix.com/v2/natural/exercise'
URL_SHEET_GET = 'https://api.sheety.co/9895274e61afcf32321df192046fbba0/100DniPyth/arkusz1'
URL_SHEET_POST = 'https://api.sheety.co/9895274e61afcf32321df192046fbba0/100DniPyth/arkusz1'

## Get info from user
exercise_text = input("Your workout: ")

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

parameters = {
    "query": exercise_text
}

response = requests.post(url=URL,json=parameters, headers=headers)
answer = response.json()

## Add a new entry

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

for item in answer["exercises"]:

    body = {
          'arkusz1': {"date": today_date,
                      "time": now_time,
                      "exercise": item['name'],
                      "duration": item['duration_min'],
                      "calories": item['nf_calories']
                    }
    }
    response_sheet = requests.post(url=URL_SHEET_POST, json=body, headers=headers)
    print(response_sheet.text)
