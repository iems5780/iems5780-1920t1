from concurrent.futures import ProcessPoolExecutor
import socket
import sys


def serve_client(client_socket, address):
    print("Serving {}".format(address))
    data = client_socket.recv(1024)
    print("Received {}".format(data.decode("utf-8")))
    client_socket.sendall(data)
    client_socket.close()

if __name__ == "__main__":
    
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind(("localhost", int(sys.argv[1])))
    soc.listen(10)
    
    with ProcessPoolExecutor(max_workers=5) as executor:
        while True:
            (client_socket, address) = soc.accept()
            executor.submit(serve_client, client_socket, address)
