import socket
import threading


def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if msg:
                print(f"\nReceived: {msg}")
        except:
            break


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 65434))

threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

while True:
    msg = input("You: ")
    client_socket.sendall(msg.encode())
