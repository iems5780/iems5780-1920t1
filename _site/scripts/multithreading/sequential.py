import time

def print_hello(n):
    time.sleep(2)
    print("Hello from {}!".format(n))

for i in range(5):
    print_hello(i)
