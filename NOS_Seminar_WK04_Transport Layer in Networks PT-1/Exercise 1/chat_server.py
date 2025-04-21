import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 65433))
print("UDP Chat Server started...")

clients = set()

while True:
    data, client_addr = server_socket.recvfrom(2048)
    message = data.decode()

    print(f"From {client_addr}: {message}")
    clients.add(client_addr)

    for client in clients:
        if client != client_addr:
            server_socket.sendto(data, client)
