API_key = "[ENTER YOUR OWN API KEY FROM OPENWEATHERMAP.ORG]"
LAT = "[Enter the latitude of your city]"
LNG = "[Enter the longitude of your city]"


Twilio_PHN_NUM = "[Enter your twilio's phone number]"
MY_PHN_NUM = "[Enter your phone number]"

import requests
from twilio.rest import Client

parameters = {
    "lat": LAT,
    "lon": LNG,
    "appid": API_key,
    "count": 4,
}

account_sid = "[your account sid from twilio]"
auth_token = "[your token from twilio]"



response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
will_rain = False

for i in range(0, len(data)):
    id = int(data["list"][i]["weather"][0]["id"])
    if id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It is going to rain today, bring your own Umbrella",
        from_=Twilio_PHN_NUM,
        to=MY_PHN_NUM,
    )
    print(message.status)