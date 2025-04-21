import socket
from encryption import encrypt_message

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 65433)

message = "Encrypted Hello, Server!"
encrypted = encrypt_message(message)

client_socket.sendto(encrypted, server_address)
client_socket.close()
