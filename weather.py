import requests

try:
    r = requests.get('https://www.metaweather.com/api/location/2455920')
except requests.exceptions.ConnectionError:
    print("Fail to connect to API")

weather = r.json()

# print(weather.keys())
for w in weather['consolidated_weather']:
    print(f"{w['applicable_date']}'s humidity is {w['humidity']}.")
