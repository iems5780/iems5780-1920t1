---
layout: page
title: Assignment 1
---

## Text Classification and Telegram Bot

* **Deadline**: 19th October, 2019 (Saturday)
* **Total Marks**: 100

In this assignment, you will build a **text classifier** of movie reviews, and then deploy the text classifier as a **chatbot** on **Telegram** to allow other people to use it. The task you will be working on is a **binary classification** problem: given a movie review, determine if it is **positive** or **negative**.

We will use a dataset of movie reviews collected from [IMDb](https://www.imdb.com/), which is a movie database where Internet users can leave their comments about movies. The dataset can be obtained from the following Webpage: [http://ai.stanford.edu/~amaas/data/sentiment/](http://ai.stanford.edu/~amaas/data/sentiment/).

Some descriptions of the dataset:
* User reviews of movies on IMDb
* A review is either labelled as **positive** or **negative**
* There are a total of 25,000 reviews grouped as a training set, and another 25,000 reviews grouped as a test set.
* There are also some unlabelled data
* Preprocessed data are also available in the compressed file

### Task 1: Text Classification (70 marks)

You will have to submit a **Jupyter notebook** for this task, which shows all your steps for training and evaluating the text classification model.

What you will have to do:

1. **Data Preparation** (15 marks)
    * Prepare a full dataset by **combining** all the training and test data found in the downloaded raw data (**DO NOT** use the preproessed data)
    * Randomly split the full dataset into a training set with **70%** of the data, and a test set with **30%** of the data (hence, you will have **35,000** reviews for training, and **15,000** reviews for testing)
    * Check that the ratio of positive to negative reviews is roughly **1:1** in both the training and test set
2. **Using a Naive Bayes Classifier** (15 marks)
    * Build a pipeline using scikit-learn's `CounterVectorizer` to **vectorize** the input data and train a **naive Bayes classifier** using the training data
    * Compute the following metrics on the test set
        - accuracy
        - precision and recall of **both positve and negative reviews**
    * Repeat the above but use the `TfidfVectorizer` instead
3. **Using a Logistic Regression Classifier** (10 marks)
    * Repeat the above experiments but use the `LogisticRegression` class in scikit-learn instead of a naive Bayes model
4. **Adding Bi-grams** (10 marks)
    * By default, the vectorizers only extract **unigrams** as features. Repeat all experiments above but adding **bigram** features.
5. **Using fastText** (15 marks) 
    * Instead of using scikit-learn, use Facebook's [fastText](https://github.com/facebookresearch/fastText) library (use the Python API)
    * You can use the default values of the parameters when training a model
    * Train a fastText model using the same training set and compute metrics on the same test set as above.
6. **Model Persistence** (5 marks)
    * Compare the accuracy scores of all the **scikit-learn models** you have built (you should have **8 models**)
    * Which model (e.g. which vectorizer + which classification model + with/without bigram) has the highest score?
    * Save that model as a file named **model.pkl**

You should keep all the steps and results in the same Jupyter notebook for submission.

### Task 2: Deploying Your Model as a Telegram Bot (30 marks)

Your next task is to deploy the selected model so that other people can use it. To skip the troubles of developing a UI for the application, you will deploy the models as a Telegram bot. Check the Telegram bot platform [https://telegram.org/blog/bot-revolution](https://telegram.org/blog/bot-revolution) and the Telegram Bot API [https://core.telegram.org/bots/api](https://core.telegram.org/bots/api).

Check also the Telepot framework for developing Telegram Bot in Python [https://github.com/nickoala/telepot](https://github.com/nickoala/telepot).

Firstly, you should create a Telegram bot by following the instructions at https://core.telegram.org/bots#3-how-do-i-create-a-bot. This bot will be used in latter assignments as well. If you are enrolled in IEMS5780, name your bot **iems_xxxxxx** where xxxxxx is your student ID.

You can easily develop a program that continuously consumes messages from a user on Telegram, process the messages, and sends back responses to the user. Below is an example bot, which will simply echo what was sent by the user.

```python
import time
import telepot
from telepot.loop import MessageLoop

def handle(msg):
    """
    A function that will be invoked when a message is
    recevied by the bot
    """
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == "text":
        content = msg["text"]
        reply = "You said: {}".format(content)
        bot.sendMessage(chat_id, reply)

if __name__ == "__main__":
    
    # Provide your bot's token
    bot = telepot.Bot("YOUR_TELEGRAM_BOT_TOKEN")
    MessageLoop(bot, handle).run_as_thread()

    while True:
        time.sleep(10)
```

Your bot should fulfil the following requirements:

* Whenever it receives a message from a user, it should pass the message into the text classification model.
* If the model predicts that it is positive, the bot should say **"This is a positive review!"**, otherwise the bot should say **"This is a negative review!"**.
* At the end of the message, you should append also the **probability of the predicted class**, up to 2 decimal places
* Your bot should NOT load the model inside the `handle` function. It should only be loaded once when the script is executed.

Below is an example of inputs and outputs:

```
Input  : This is a wonderful movie!
Output : This is a positive review! (0.89)

Input  : I will not recommend this movie to my friends
Output : This is a negative review! (0.76)
```

**Note:** You do not need to keep your script running for marking. We will execute the script to test if necessary. Make sure you have the telegram bot token written inside the source code.

### What to Submit

You should prepare **two files** to be submitted for this assignment:
* **classifiers.ipynb**: the Jupyter notebook in which you have done Task 1, including all the source codes and results
* **bot.py**: the script in which you implement the Telegram bot to perform text classification on user inputs

You should put these two files in a folder named <student_id>_assignment1 (e.g. 12345678_assignment1), and compress it into a zip file (e.g. 12345678_assignment1.zip). Submit the compressed file to Blackboard.
