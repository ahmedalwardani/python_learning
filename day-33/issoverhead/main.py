import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 45.341480
MY_LONG = -75.626190
MY_EMAIL = "ahmed.alwardani.1995@gmail.com"
PASSWORD = "yrzafyvxammkdtkk"
GMAIL_HOST = "smtp.gmail.com"

def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    sunrise_sunset_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    sunrise_sunset_response.raise_for_status()
    sunrise_sunset_response_data = sunrise_sunset_response.json()
    sunrise = int(sunrise_sunset_response_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sunrise_sunset_response_data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP(GMAIL_HOST)
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject: Look Up👆\n\nThe ISS is above you in "
                                                                       f"the sky!")



#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



