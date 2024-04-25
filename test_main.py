import pytest
from main import get_weather, print_weather_info


def test_get_weather():
    city_name = "London"
    response = get_weather(city_name)
    assert response['name'] == city_name
    assert 'main' in response
    assert 'temp' in response['main']


def test_print_weather_info(capsys):
    response = {'name': 'London', 'main': {'temp': 20}}
    print_weather_info(response)
    captured = capsys.readouterr()
    assert "Weather information:" in captured.out
    assert "London - 20°C" in captured.out
