import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 65436))
server_socket.listen(1)

print("Server waiting for weather data...")
client_socket, addr = server_socket.accept()
data = client_socket.recv(1024)
print(f"Weather update: {data.decode()}")

client_socket.close()
server_socket.close()
