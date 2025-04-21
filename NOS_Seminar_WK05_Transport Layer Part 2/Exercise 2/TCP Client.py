
import socket
import datetime

start_time = datetime.datetime.now()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 65432))
message = "Hello TCP"
client_socket.sendall(message.encode())
response = client_socket.recv(1024)
end_time = datetime.datetime.now()

print(f"TCP Response: {response.decode()}")
print(f"Time taken (TCP): {end_time - start_time}")
client_socket.close()
