import socket

import requests

def fetch_weather_details(lat, lon):
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(api_url)
    if response.status_code == 200:
        weather = response.json()["current_weather"]
        return f"Temp: {weather['temperature']}°C, Wind: {weather['windspeed']} km/h"
    return "Weather data not available"


weather_message = fetch_weather_details(51.5225, -0.1304)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 65433)
client_socket.sendto(weather_message.encode(), server_address)
print("Detailed weather data sent!")
client_socket.close()
