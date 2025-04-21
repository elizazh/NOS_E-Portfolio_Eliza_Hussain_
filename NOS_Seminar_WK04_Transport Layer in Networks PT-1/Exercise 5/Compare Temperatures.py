import socket
import requests


def fetch_temp(lat, lon):
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(api_url)
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data["current_weather"]["temperature"]
    return None


# Coordinates
uni_coords = (51.5225, -0.1304)

library_coords = (51.5299, -0.1270)

uni_temp = fetch_temp(*uni_coords)
lib_temp = fetch_temp(*library_coords)

message = f"University Temp: {uni_temp}°C, British Library Temp: {lib_temp}°C"

# Send via UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 65433)
client_socket.sendto(message.encode(), server_address)
print("Temperature comparison sent!")
client_socket.close()
