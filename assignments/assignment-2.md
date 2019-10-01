# IEMS5780 / IERG4080 Assignment 2

## Image Classification and Telegram Bot

* **Deadline**: 9th November, 2018 (Friday)
* **Total Marks**: 100

## Objectives

* To try using existing deep learning frameworks to classify images using pre-trained models
* To get familiar with socket programming in Python
* To get familiar with message passing between threads and processes in Python

## Tasks

In this assignment, you will build an **image classifier** and then deploy the classifier as a **chatbot** on **Telegram**. You will NOT be required to train your own model, as the focus would be on socket programming and multi-threaded programming in Python.

You will build a system which offer image classification service via Telegram bot. A user in Telegram can either send **an image** or **the URL of an image** to the bot, and the bot will feed the image (download the image first if it is given a URL) into a deep learning model to generate image classification predictions, and then send back the result to the user.

<img src="assignment2-system.png" width="100%"/>

The overall architecture of the system is shown in the diagram above. The details of each component will be described below.

## The Bot Script

In the Bot Script (`bot.py`), you should implement logic that performs the following:

* Continuously receiving user messages from Telegram
* Whenever a message is received, **if** the message contains an **image**, or **if** the message's text has an URL inside, get the binary data of the image, and send it via a **TCP connection** to the server
* If the message does not contain an image or a URL to an image, **nothing** has to be done
* Once classification results are received from the server, **format** the output and send the results back to the user

Your script should have at least **three threads** running. Each thread will be responsible for different operations. The threads **should NOT share any variables**, and data between different threads should be passed using **queues**.

### Thread 1 - Receiving Messages

You can re-use part of the scripts you wrote in Assignment 1 to listen for messages the user sends via Telegram. You can assume that the message can be of one of the following **two types**:

1. The message contains only **text**, which is a **URL** to an image on the Web
2. The message contains a **photo** (refers to Telegram's [API documentation](https://core.telegram.org/bots/api#message) to see how to retrieve the photo from Telegram)

In this thread, you should keep getting messages from Telegram. Once a message is received, you should extract the image (either from the given URL or from Telegram), and pass the **image object** as well as the **chat_id** to **Thread 2** by putting it into **Queue 1**.

**Hint 1**:

You can use the following code to download the photo from Telegram.

```python
if content_type == 'photo':
    bot.download_file(msg['photo'][-1]['file_id'], 'file.png')
```

**Hint 2**:

You can load an image from a file using the [Pillow](https://pillow.readthedocs.io/en/5.3.x/) package:

```python
from PIL import Image

image = Image.open('file.png')
```

### Thread 2 - Client Thread

This thread keeps getting data from **Queue 1**. Once data is obtained form the queue, it should create a socket and attempt to establish **a new TCP connection** to the server.

Once the connection is established, it should **send the image as well as the chat_id** to the server, and then wait for the response from the server. Since the data sent to the server should be a **string**, you should first create a **dictionary** containing the data, and then use `json.dumps` to convert it into a JSON-encoded string.

You will need to implement your own method for determining whether a message is **fully received** on both the client side and the server side. For example, you can append a special string such as `##END##` at the end of the message to delimit the message.

Note that you should have received **an image object** from **Queue 1**. You should **encode the binary data** into string such that it can be sent over the TCP connection. One way of doing this is to convert the image object into a **base64 encoded** string:

```python
import base64
from io import BytesIO
from PIL import Image

image = Image.open('file.png')
buffered = BytesIO()
image.save(buffered, format="PNG")
encoded_image = base64.b64encode(buffered.getvalue())
```

Thus, the dictionary that will be encoded using `json.dumps` would be something like the following:

```python
data = {
    'image': <base64-encoded string of the image object>,
    'chat_id': <chat id as received from Telegram>
}
```

When the response from the server is received, this thread should put the response into **Queue 2**.

### Thread 3 - Sending Messages

This thread keeps getting data from **Queue 2**. Once data is received, it should format the output and send a message back to the user via Telegram.

The message sent to the user should contain the **top 5 classes** predicted by the model in the server. As an example, if a photo of a container ship is received from the user, the message sent to the user should look like below:

```
1. container_ship (0.4625)
2. lifeboat (0.1579)
3. wreck (0.1383)
4. pop_bottle (0.0477)
5. dock (0.0406)
```

## The Server

In the `server.py` script, you will need to implement a **TCP server**, in which there are **two threads** running (including the main thread). The **main thread** will be responsible for **listening for incoming connections** from clients. Once a client is connected, it should pass throught a queue the client socket to the **second thread**, which will communicate with the client.

The second thread should pre-load a **Keras pre-trained ResNet50 model** when it is first started. It will then continuously getting data from the queue. Given a client socket, it will read the message from the client, first **decode the JSON data**, and then **decode the base64-encoded image data**. It should then feed the image into the neural network, and obtain the predicted classes as well as the probabilities.

**Hint 1**: The base64-encoded image can be decoded using the following code:

```python
import base64
image_data = base64.b64decode(encoded_image)
with open('image.png', 'wb') as outfile:
    outfile.write(image_data)
```

Once the predictions are generated, the second thread should compose a dictionary containing the **top 5** predictions, as well as the **chat_id** in the original message as in the example below:

```python
{
    "predictions": [
        {"label": "container_ship", "proba": 0.4625},
        {"label": "lifeboat", "proba": 0.1579},
        {"label": "wreck", "proba": 0.1383},
        {"label": "pop_bottle", "proba": 0.0477},
        {"label": "dock", "proba": 0.0406},
    ],
    "chat_id": <chat_id>
}
```

This dictionary should be JSON-encoded, and then sent back to the client.

## What to Submit

You should prepare **two files** to be submitted for this assignment:
* **bot.py**: the script in which you implement the Telegram bot
* **server.py**: the script in which you implement the server deploying the image classification model

You should put these two files in a folder named <student_id>_assignment1 (e.g. 12345678_assignment2), and compress it into a zip file (e.g. 12345678_assignment2.zip). Submit the compressed file to Blackboard.
