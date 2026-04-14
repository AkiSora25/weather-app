from app.services.weather_api import get_coordinates, get_weather
from app.utils.formatter import convert_temperature


def main():
    city = input("Inserisci una città: ")
    
    coords = get_coordinates(city)
    if coords is None:
        return
    
    lat, lon = coords
    temperature = get_weather(lat, lon)
    
    print(f"La temperatura attuale a {city} è {temperature}°C")


if __name__ == "__main__":
    main()

