
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 65433)

message = b"Hello, UDP Server!"
client_socket.sendto(message, server_address)
client_socket.close()
