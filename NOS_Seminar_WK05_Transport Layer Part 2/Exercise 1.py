import socket
import datetime

# CreatING TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting to the server
client_socket.connect(('localhost', 65432))

# Input message from user
message = input("Enter message: ")

# Recording the time just before sending
start_time = datetime.datetime.now()

# Sending message to server
client_socket.sendall(message.encode())

# Wait and receive response from server
response = client_socket.recv(1024)

# Record time after receiving the response
end_time = datetime.datetime.now()

# Print server response
print(f"Server response: {response.decode()}")


time_taken = end_time - start_time
print(f"Time taken to send and receive: {time_taken.total_seconds()} seconds")


client_socket.close()
