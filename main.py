import httpx
import json


cities = {
    "chicago": {"lat": 41.8781, "lon": -87.6298},
    "new york": {"lat": 40.7128, "lon": -74.0060},
    "los angeles": {"lat": 34.0522, "lon": -118.2437}
}


def get_weather(city_name):
    city_name = city_name.lower()
    if city_name in cities:
        lat = cities[city_name]["lat"]
        lon = cities[city_name]["lon"]
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        response = httpx.get(url)
        if response.status_code == 200:
            data = response.json()
            current_weather = data.get('current_weather', None)
            if current_weather:
                temperature = current_weather.get('temperature', 'N/A')
                windspeed = current_weather.get('windspeed', 'N/A')
                print(f"\nCurrent weather in {city_name.capitalize()}:")
                print(f"Temperature: {temperature}°C")
                print(f"Windspeed: {windspeed} km/h")
            else:
                print("No current weather available")
        else:
            print("Unable to load in.")
    else:
        print("City not found.")
            
while True:
    get_weather(city_name = input("Available cities: Chicago, New York, Los Angeles \n Enter a city: "))
    end = input("Would you like to end? (yes/no)").lower()
    if end == "yes":
        break
    else:
        continue
    
