import json
import requests
import os
from dotenv import load_dotenv


def get_forcast(api_key):
    city = input("What city would you like to know the weather for?\n>>> ")

    r = requests.get(
        f"https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=3"
    )

    data = json.loads(r.text)
    week = data["forecast"]["forecastday"]

    print(f"Here is the weather for 3 days in {city}:")

    for day in week:
        print(
            f"The high for {day['date']} is {day['day']['maxtemp_c']} degrees Celsius"
        )
        print(f"The low for {day['date']} is {day['day']['mintemp_c']} degrees Celsius")
        print(f"The condition for {day['date']} is {day['day']['condition']['text']}")
        print()

    input()


def get_current_weather(api_key):
    city = input("What city would you like to know the weather for?\n>>> ")

    r = requests.get(
        f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    )

    data = json.loads(r.text)
    location = data["location"]["name"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    feels = data["current"]["feelslike_c"]

    print(
        f"The weather in {location} is currently {temp_c} degrees but it feels like {feels} degrees, it's looking to be {condition}"
    )

    input()


def main():
    load_dotenv()

    while True:
        api_key = os.getenv("KEY")

        print("Welcome to Love Data Week!")
        print("What would you like to do?")
        print("1. Get Current Weather")
        print("2. Get Weather Forecast")
        option = input(">>> ")

        if option == "1":
            get_current_weather(api_key)
        elif option == "2":
            get_forcast(api_key)


if __name__ == "__main__":
    main()
