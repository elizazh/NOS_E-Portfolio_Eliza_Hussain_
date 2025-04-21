import socket
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 65433)


def receive():
    while True:
        data, _ = client_socket.recvfrom(2048)
        print("\nMessage:", data.decode())


def send():
    while True:
        msg = input("You: ")
        client_socket.sendto(msg.encode(), server_address)


threading.Thread(target=receive, daemon=True).start()
send()
