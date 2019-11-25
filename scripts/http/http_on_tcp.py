import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to Web server of CUHK
# By default a web server runs on port 80
s.connect(("www.google.com.hk", 80))

# Create an HTTP request and send it to server
req = "GET / HTTP/1.1\n" \
      "Host: www.google.com.hk\n" \
      "Accept-Language: en\n" \
      "\r\n".encode("ascii")

s.sendall(req)

# Read the HTTP response from the server
response = s.recv(1024)
print(response)
