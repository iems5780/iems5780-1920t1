import socket

# Note, the second parameter for socket() is socket.SOCK_DGRAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind it to an IP address and a port
server_socket.bind(("localhost", 50000))

while True:
    # data is the data sent from a client
    # address is the IP address of the client
    data, address = server_socket.recvfrom(1024)
    print("Received '{}' from {}".format(
        data.decode("utf-8"), address))
