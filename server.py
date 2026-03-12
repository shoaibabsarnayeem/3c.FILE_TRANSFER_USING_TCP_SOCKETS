import socket

# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 12345

# Bind socket
server.bind((host, port))

# Listen for client
server.listen(1)
print("Server waiting for connection...")

conn, addr = server.accept()
print("Connected to:", addr)

# Open file and send data
file = open("sample.txt", "rb")
data = file.read()

conn.send(data)

print("File sent successfully")

file.close()
conn.close()