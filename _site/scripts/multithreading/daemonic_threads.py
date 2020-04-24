from threading import Thread
from time import sleep


def print_hello():
    sleep(0.2)
    print("Hello!")

if __name__ == "__main__":
    threads = []
    for i in range(5):
        t = Thread(target=print_hello, daemon=True)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


