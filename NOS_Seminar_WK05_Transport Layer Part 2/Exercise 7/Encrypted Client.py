from cryptography.fernet import Fernet
import socket

key = Fernet.generate_key()
cipher = Fernet(key)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 65435))

message = "Secret Message"
encrypted = cipher.encrypt(message.encode())
client_socket.sendall(encrypted)
client_socket.close()
