"""
A sample non-blocking TCP socket server that echoes
what the clients send out.
"""
import sys
import select
import socket
import sys
import queue

# Create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set blocking to False
server.setblocking(0)

# Bind the socket to the port
server.bind(("localhost", int(sys.argv[1])))

# Listen for incoming connections
server.listen(10)
print("Start listening on localhost:{}".format(int(sys.argv[1])))

# Sockets from which we will READ
inputs = [server]

# Sockets from which we will WRITE
# (we don't have any at this moment)
outputs = []

# Messages that will be sent out
message_queues = {}

while True:

    # Wait for at least one of the sockets to be ready
    print("Waiting for sockets to be available")
    readable, writable, errors = select.select(inputs,
                                                    outputs,
                                                    inputs)
    
    # Check each readable sockets
    for s in readable:

        if s is server:
            # The server socket is ready to be read
            # meaning that there is a client wanting to connect
            client_socket, client_address = s.accept()
            print("Accepted connection from {}".format(client_address))
            client_socket.setblocking(0)  # set socket to non-blocking
            
            # client socket is a socket that we want to read from
            # therefore we add it to the inputs list
            inputs.append(client_socket)

            # Give the connection a queue for data
            # we want to send
            message_queues[client_socket] = queue.Queue()

        else:
            # It is one of the client sockets which is ready to be read
            # We read data from it
            data = s.recv(1024)
            if data:
                # Data is received from a client socket
                print("Received {} from {}".format(data, s.getpeername()))
                
                # Put the data into the corresponding queue
                message_queues[s].put(data)
                
                # Given that we have received data from this client
                # we may want to send data to the client
                # so we add this socket to the outputs list
                if s not in outputs:
                    outputs.append(s)

            else:
                # If data is empty, it means the client has disconnected
                print("Connection to {} is closed".format(s.getpeername()))
                
                # Remove the socket from all the lists
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)

                # Close the connection on server side
                s.close()

                # Remove socket's message queue
                del message_queues[s]

    # Check each writable sockets
    for s in writable:
        try:
            # Try to get data from message queue of the socket
            # using a non-blocking function
            # (it throws exception if the queue is empty)
            next_msg = message_queues[s].get_nowait()
        except queue.Empty:
            # No message has to be sent to the client
            # we can remove it from the outputs list
            print("{}'s queue is empty".format(s.getpeername()))
            outputs.remove(s)
        else:
            # There is something that needs to be sent to the client
            print("Sending {} to {}".format(next_msg, s.getpeername()))
            s.send(next_msg)

    # Check each socket with errors
    for s in errors:
        print("Error on {}".format(s.getpeername()))
        # Remove it from all lists
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)

        # Close the connection and delete its message queue
        s.close()
        del message_queues[s]
