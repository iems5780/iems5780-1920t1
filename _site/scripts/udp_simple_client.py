import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address and port number, and message to be sent
server_address = ("localhost", 50000)

message = "I love socket programming in Python!"
bytes_send = client_socket.sendto(message.encode("utf-8"), server_address)

# Close the socket
client_socket.close()
