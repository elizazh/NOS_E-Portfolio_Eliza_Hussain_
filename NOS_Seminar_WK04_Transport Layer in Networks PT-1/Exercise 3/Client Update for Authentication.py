import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 65433)

# Step 1: Here i Authenticate
auth_message = "user1,pass123"
client_socket.sendto(auth_message.encode(), server_address)

response, _ = client_socket.recvfrom(2048)
print(response.decode())

# Step 2: If authenticated, SHOULD send chat message
if response.decode() == "Authenticated!":
    message = "This is a secure message."
    client_socket.sendto(message.encode(), server_address)

client_socket.close()
