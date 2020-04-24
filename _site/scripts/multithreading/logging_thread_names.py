import logging
import threading

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("TIME=%(asctime)s, %(threadName)s, [%(levelname)s] : %(message)s")
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)


def print_log():
    logger.info("Hello!")

for i in range(5):
    threading.Thread(target=print_log, args=()).start()

for t in threading.enumerate():
    if t != threading.main_thread():
        t.join()
