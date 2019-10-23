import socket

# create an INET TCP socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server (change localhost to an IP address if necessary)
soc.settimeout(5)
soc.connect(("localhost", 50000))
print("Connected to server")

# Send a message to the server
msg = "Hello Server!".encode("utf-8")
soc.send(msg)

# Receive data from the server
data = soc.recv(1024)
print("Sent {} to server.".format(data.decode("utf-8")))

# Always close the socket after use
soc.close()
