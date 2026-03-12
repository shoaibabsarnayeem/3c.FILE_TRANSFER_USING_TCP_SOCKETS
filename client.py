import socket

# Create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 12345

# Connect to server
client.connect((host, port))

# Receive file data
data = client.recv(1024)

# Write into file
file = open("received.txt", "wb")
file.write(data)

print("File received successfully")

file.close()
client.close()