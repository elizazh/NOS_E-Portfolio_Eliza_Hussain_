import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 65433))
print("UDP Server is ready to receive messages...")

clients = {}

while True:
    data, client_address = server_socket.recvfrom(2048)
    decoded_data = data.decode()
    print(f"Received from {client_address}: {decoded_data}")

    if client_address[0] not in clients:
        clients[client_address[0]] = [decoded_data]
    else:
        clients[client_address[0]].append(decoded_data)

    print(f"Current clients data: {clients}")
