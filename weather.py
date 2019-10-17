# To test your code, open a terminal below and run:
#   python3 weather.py


import requests

API_ROOT = 'https://www.metaweather.com'
API_LOCATION = '/api/location/search/?query='
API_WEATHER = '/api/location/'  # + woeid

def fetch_location(query):
    try:
        return requests.get(API_ROOT + API_LOCATION + query).json()
    except requests.exceptions.ConnectionError:
        print("Failed to connect to server!")
        return ""

def fetch_weather(woeid):
    try:
        return requests.get(API_ROOT + API_WEATHER + str(woeid)).json()
    except requests.exceptions.ConnectionError:
        print("Failed to connect to server!")
        return ""

def display_weather(weather):
    print(f"Weather for {weather['title']}:")
    # print(weather.keys())
    for w in weather['consolidated_weather']:
        print(f"{w['applicable_date']}: {w['weather_state_name']}. Max temp is {round(w['max_temp'],1)}, min temp is {round(w['min_temp'],1)}, humidity is {w['humidity']}.")

def disambiguate_locations(locations):
    print("Ambiguous location! Did you mean:")
    for loc in locations:
        print(f"\t* {loc['title']}")

def weather_dialog():
    where = ''
    while not where:
        where = input("Where in the world are you? ")
    locations = fetch_location(where)
    if len(locations) == 0:
        print("I don't know where that is.")
    elif len(locations) > 1:
        disambiguate_locations(locations)
    else:
        woeid = locations[0]['woeid']
        d = fetch_weather(woeid)
        if len(d)!= 0:
            display_weather(d)


if __name__ == '__main__':
    while True:
        weather_dialog()
