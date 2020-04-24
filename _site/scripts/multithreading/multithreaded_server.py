import sys
import socket
import logging
from threading import Thread


def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s, %(threadName)s, [%(levelname)s] : %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def serve_client(client_socket, address):
    logger.info("Serving client from {}".format(address))
    data = client_socket.recv(1024)
    client_socket.sendall(data)
    client_socket.close()
    logger.info("Finished")


if __name__ == "__main__":

    logger = get_logger()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", int(sys.argv[1])))
    server_socket.listen(10)
    logger.info("Server starts listening for connection...")

    while True:
        (client_socket, address) = server_socket.accept()
        logger.info("Accepted connection from {}".format(address))
        client_thread = Thread(target=serve_client,
                               args=(client_socket, address),
                               daemon=True)
        client_thread.start()
