import requests
from datetime import datetime
import os

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
GENDER = "male"
WEIGHT_KG = 75
HEIGHT_CM = 173
AGE = 28
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]

today_exercise = input("Tell me which exercises you did: ")

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

nutritionix_params = {
    "query": today_exercise
}

nutritionix_response = requests.post(url=NUTRITIONIX_ENDPOINT, json=nutritionix_params, headers=nutritionix_headers)
nutritionix_response.raise_for_status()

today_date = datetime.now().strftime("%d/%m/%y")
time_now = datetime.now().strftime("%X")

for exercise in nutritionix_response.json()["exercises"]:
    sheety_record = {
        "workout": {
            "exercise": exercise["name"].title(),
            "date": today_date,
            "time": time_now,
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheety_headers = {"Authorization": os.environ["TOKEN"]}

sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_record, headers=sheety_headers)
sheety_response.raise_for_status()
print(sheety_response.json())
