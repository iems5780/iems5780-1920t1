import time
from redis import StrictRedis

# Get a connection to Redis
queue = StrictRedis(host='localhost', port=6379)

# Publish a message to a channel called testing
message = "Hello World {}"

for i in range(100):
    m = message.format(i)
    queue.publish("testing", m.encode("utf-8"))
    print("Send {} to redis.".format(m))
    time.sleep(2)
