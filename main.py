import requests
from dotenv import load_dotenv
import os


def get_weather(city_name):
    """
    Fetches the weather information for a given city.

    Parameters:
    city_name (str): The name of the city for which to fetch the weather information.

    Returns:
    dict: A dictionary containing the weather information for the city.
    """
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    query_string = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(query_string).json()
    return response


def print_weather_info(response):
    """
    Prints the weather information for a city.

    Parameters:
    response (dict): A dictionary containing the weather information for a city.

    Returns:
    None
    """
    print(f"Weather information: ")
    print(f"{response['name']} - {response['main']['temp']}°C")
