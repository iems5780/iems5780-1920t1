import socket
import time

# create an INET socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to the host and a port
server_socket.bind(("localhost", 50000))

# Listen for incoming connections from clients
server_socket.listen(1)

# A indefinite loop
while True:
    # accept connections from outside
    (client_socket, address) = server_socket.accept()
    print("accepted connection from %s" % str(address))

    # Read data from client and send it back
    data = client_socket.recv(1024)
    print("Received %s from %s" % (data.decode("utf-8"), address))
    client_socket.sendall(data)

    # Close the socket
    client_socket.close()
