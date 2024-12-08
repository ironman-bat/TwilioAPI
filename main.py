import requests  # Ensure the requests module is installed
from twilio.rest import Client  # Ensure the twilio module is installed

# The correct API endpoint and keys should be used
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "cae2c5a9272954900324ee8968a23ff6"  # Use a valid OpenWeatherMap API key
account_sid = "01928300a080a808028em"  # Replace with valid Twilio account SID
auth_token = "u923094820384nc2903284_"  # Replace with valid Twilio auth token

weather_params = {
    "lat": 46.947975,
    "lon": 7.447447,
    "appid": api_key,
    "cnt": 4,  # Number of forecasted hours
}

# Ensure API response is successful
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # Ensure to use correct Twilio numbers
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+2676425037",  # Replace with your Twilio number
        to="6477010945"  # Replace with your real phone number
    )
    print(message.status)
