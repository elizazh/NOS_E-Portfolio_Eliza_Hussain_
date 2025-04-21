import socket
from encryption import decrypt_message

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 65433))
print("Secure UDP Server is ready...")

while True:
    data, client_address = server_socket.recvfrom(2048)
    decrypted = decrypt_message(data)
    print(f"Encrypted message from {client_address}: {decrypted}")
