import requests
from dotenv import load_dotenv
import os


def get_weather(city_name):
    load_dotenv()
    # city_name = input("Enter required city name: ")
    API_KEY = os.getenv("API_KEY")
    query_string = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    responce = requests.get(query_string).json()
    return responce


def print_weather_info(responce):
    print(f"Weather information: ")
    print(f"{responce['name']} - {responce['main']['temp']}°C")
