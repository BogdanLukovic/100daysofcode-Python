import requests
import json
import os
from smtplib import *


def send_mail():
    my_email = os.getenv("MAIL_MAILBLAZER")
    print(my_email)
    password = "jpdpnklvroznjwip"

    letter_with_subject = f"Subject:Bring an umbrella! \n\nIt's going to rain in the next 12 hours."

    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=letter_with_subject)

        print("Mail sent.")

TWILLIO_PASSWORD = "x'5iG#3BjCF',@xasadvxcesr"

OWM_Endpoint = "http://api.openweathermap.org/data/2.5/forecast"
OWM_params = {
    # "lat": 44.01,
    # "lon": 20.91,
    "lat": 51.51,
    "lon": 0.13,
    "units": "metric",
    "appid": "ac7e8a1db9f1a8ca704a984ae00b954e",
}
response = requests.get(OWM_Endpoint, params=OWM_params)
weather_forcast = response.json()["list"]
# print(weather_forcast)

forcast = 39
will_rain = False

for day in range(forcast):
    # print(weather_forcast[day]["weather"][0]["id"])
    # print(weather_forcast[day]["weather"][0]["main"])
    for weather_condition in weather_forcast[day]["weather"]:
        if weather_condition["id"] < 700:
            will_rain = True

if will_rain:
    send_mail()



