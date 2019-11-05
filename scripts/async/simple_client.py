import socket
import sys

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(("localhost", int(sys.argv[1])))

soc.sendall(b"Hello")
data = soc.recv(1024)
soc.close()
