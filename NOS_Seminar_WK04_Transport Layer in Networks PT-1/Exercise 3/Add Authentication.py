import socket

AUTH_CREDENTIALS = {
    "user1": "pass123",
    "admin": "adminpass"
}


def authenticate(data):
    try:
        username, password = data.decode().split(",")
        return AUTH_CREDENTIALS.get(username) == password
    except:
        return False


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 65433))
print("UDP Server is running...")

authenticated_clients = set()

while True:
    data, client_address = server_socket.recvfrom(2048)
    if client_address not in authenticated_clients:
        if authenticate(data):
            server_socket.sendto(b"Authenticated!", client_address)
            authenticated_clients.add(client_address)
            print(f"{client_address} authenticated.")
        else:
            server_socket.sendto(b"Authentication Failed", client_address)
    else:
        print(f"Message from {client_address}: {data.decode()}")
