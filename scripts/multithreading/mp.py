import time
# Import the Process class
from multiprocessing import Process

# A function to print Hello World
def f(i):
    while True:
        i += 1
        time.sleep(0.001)


if __name__ == '__main__':  # important!
    processes = []
    for i in range(3):
        p = Process(target=f, args=(i, ))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
