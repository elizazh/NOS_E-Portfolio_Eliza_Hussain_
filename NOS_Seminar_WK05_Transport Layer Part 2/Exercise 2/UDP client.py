
import socket
import datetime

start_time = datetime.datetime.now()

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 65433)
message = "Hello UDP"
udp_socket.sendto(message.encode(), server_address)
end_time = datetime.datetime.now()

print("Message sent via UDP")
print(f"Time taken (UDP): {end_time - start_time}")
udp_socket.close()

