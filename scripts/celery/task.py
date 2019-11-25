import time
import random
from celery import Celery

# Create a Celery app, providing a name and the URI to the message broker
# Here we assume Redis is installed and running
app = Celery('tasks', broker='redis://localhost')

# Create a task using the app.task decorator
@app.task
def generate_squares(n):
    for i in range(n):
        print(i * i)
        time.sleep(random.randint(1,3))  # simulate a long running task
