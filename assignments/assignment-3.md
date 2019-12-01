---
layout: page
title: Assignment 3
---

## Asynchronous Messaging

* **Deadline**: 21st December, 2019 (Saturday)
* **Total Marks**: 100

## Objectives

* To get familiar with using **asynchronous messaging** in network applications

## Tasks

In this assignment, you will create an application that performs object recognition using a deep learning model, which is very similar to the one in Assignment 2. However, we will make some changes to the system by replacing direct TCP connections with **asychronous messaging** using **Redis**.

**Please note** that we will NOT use Telegram in this assignment.

The following diagram illustrate the **system architecture** of the application.

<img src="{{site.baseurl}}assignments/assignment-3-system.png" width="100%"/>

There are three components in this system:
1. **`main.py`**: a program that keep reading user input from the command prompt, and is also responsible for printing out the results for the user to read
2. **`image_downloader.py`**: a program that is responsible for downloading images from either Telegram or a given URL
3. **`predict.py`**: a program that loads a PyTorch pre-trained model for object recognition, and generates predictions when given an image

**NOTE** that you should NOT use the publish/subscribe mechanism of Redis in this assignment. You should use **lists** in Redis to implement message queues. Refer to the slides in Lecture 11 for more information: [Lecture 11 Slide 28]({{site.baseurl}}public/lectures/lecture-11.html#28)

### The Main Script

In the Main Script (`main.py`), you should implement logic that performs the following:

* **In one thread**, continuously prompt user on the command line for an Image URL (See example below)
* Whenever a URL is received, create a message and submit it to a message queue in Redis named **`download`**. The message should be JSON-encoded, which contains the following data:
    1. `timestamp` (the time at which the URL is submitted, in YYYY-mm-dd HH:MM:SS format)
    2. `url` of the image
* In **another thread**, keep listening for message from another message queue named **`prediction`**. The message from that queue should contains the predictions, the URL, and the timestamp of the request from the user. **Print** the results on the screen. (see example below)
* If the user does not input a valid URL (i.e. not starting with `http://` or `https://`), **nothing** should be done.

Example inputs and outputs:

```python
Please input the URL of the image: https://image.cnbcfm.com/api/v1/image/105972971-1560808092256preview.jpg?v=1560808098&w=678&h=381

Results:
URL: https://image.cnbcfm.com/api/v1/image/105972971-1560808092256preview.jpg?v=1560808098&w=678&h=381
1. airliner (0.6940)
2. wing (0.2234)
3. space_shuttle (0.0125)
4. moving_van (0.0052)
5. trailer_truck (0.0031)
```

### The Image Downloading Script

In the Image Downloading Script (`image_downloader.py`), you should implement logic that performs the following:

* Continuously receiving messages from the message queue **`download`** in Redis.
* Once a message is recevied, you should download the image from the URL
* Encode the binary data of the image and submit a message to a message in Redis named **`image`**. The message should be JSON-encoded, which contains the following data:
    1. `timestamp` (the time at which the URL is submitted, in YYYY-mm-dd HH:MM:SS format)
    2. `url` of the image
    2. `image`, the base64-encoded binary data of the image

### The Prediction Script

In the Prediction Script (`predict.py`), you should pre-load a **PyTorch pre-trained InceptionV3 model** when it is first started.

In this script, you should implement logic that performs the following:
* Continuously receiving messages from the message queue **`image`** in Redis.
* Once a message is received, decode the image data in the message, preprocess it, and feed it into the PyTorch model to generate predictions
* Once you have the predictions, submit a message to the message queue `prediction` so that the Bot Script can receive the predictions. You only need to send back the **top 5** predicted labels. The message should be in the following format (similar to Assignment 2, and JSON-encoded):

```python
{
    "predictions": [
        {"label": "container_ship", "score": 0.4625},
        {"label": "lifeboat", "score": 0.1579},
        {"label": "wreck", "score": 0.1383},
        {"label": "pop_bottle", "score": 0.0477},
        {"label": "dock", "score": 0.0406},
    ],
    "url": "http://...."
}
```

### Load Balancing

Once you have finished all the scripts. You can experiment with starting multiple instance of `image_downloader.py` and `predict.py`. You should see that they will consume messages from the message queues alternatively, which the need to do any configurations on the scripts.

## What to Submit

You should prepare **three files** to be submitted for this assignment:
* **main.py**: the script in which you implement the main program
* **image_downloader.py**: the script in which you implement the image downloading logic
* **predict.py**: the script in which you implement the logic of generating predictions using a pre-trained PyTorch model

You should put these two files in a folder named <student_id>_assignment3 (e.g. 12345678_assignment3), and compress it into a zip file (e.g. 12345678_assignment3.zip). Submit the compressed file to Blackboard.
