import socket
import threading

clients = []


def handle_client(client_socket, addr):
    print(f"[+] New connection from {addr}")
    while True:
        try:
            msg = client_socket.recv(1024)
            if not msg:
                break
            for client in clients:
                if client != client_socket:
                    client.sendall(msg)
        except:
            break
    client_socket.close()
    clients.remove(client_socket)
    print(f"[-] {addr} disconnected")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 65434))
server.listen(5)
print("Multi-client server listening...")

while True:
    client_socket, addr = server.accept()
    clients.append(client_socket)
    threading.Thread(target=handle_client, args=(client_socket, addr)).start()
