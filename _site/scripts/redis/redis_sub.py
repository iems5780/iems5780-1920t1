import time
from redis import StrictRedis

# Connect and subscribe
queue = StrictRedis(host='localhost', port=6379)
pubsub = queue.pubsub()
pubsub.subscribe('testing')
# The first message you receive will be a confirmation of subscription
message = pubsub.get_message()
print("The first message received:")
print(message)

while True:
    print("Waiting for a message...")
    message = pubsub.get_message()
    if message:
        print("Received {}".format(message))
    else:
        time.sleep(1)
