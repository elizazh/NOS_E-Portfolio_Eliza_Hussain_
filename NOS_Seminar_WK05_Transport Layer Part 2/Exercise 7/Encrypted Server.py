from cryptography.fernet import Fernet
import socket

key = Fernet.generate_key()
cipher = Fernet(key)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 65435))
server_socket.listen(1)

client_socket, addr = server_socket.accept()
data = client_socket.recv(1024)
decrypted = cipher.decrypt(data)
print(f"Decrypted message: {decrypted.decode()}")

client_socket.close()
server_socket.close()
