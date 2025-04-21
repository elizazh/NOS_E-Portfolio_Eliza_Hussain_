import socket
import requests

api_url = "https://api.open-meteo.com/v1/forecast?latitude=51.47&longitude=0.0363&current_weather=true"
response = requests.get(api_url)

if response.status_code == 200:
    temp = response.json()['current_weather']['temperature']
    message = f"Current temperature: {temp}°C"
else:
    message = "Failed to fetch data"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 65436))
client_socket.sendall(message.encode())
client_socket.close()
