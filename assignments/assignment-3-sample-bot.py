import time
import logging
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardButton, InlineKeyboardMarkup
 
logging.basicConfig(level=logging.INFO)


def handle(msg):
    """
    A function that will be invoked when a message is
    recevied by the bot
    """
    # Get text or data from the message
    text = msg.get("text", None)
    data = msg.get("data", None)

    if data is not None:
        # This is a message from a custom keyboard
        chat_id = msg["message"]["chat"]["id"]
        content_type = "data"
    elif text is not None:
        # This is a text message from the user
        chat_id = msg["chat"]["id"]
        content_type = "text"
    else:
        # This is a message we don't know how to handle
        content_type = "unknown"
    
    if content_type == "text":
        message = msg["text"]
        logging.info("Received from chat_id={}: {}".format(chat_id, message))

        if message == "/start":
            # Check against the server to see
            # if the user is new or not
            # TODO
            bot.sendMessage(chat_id, "Welcome!")
        
        elif message == "/rate":
            # Ask the server to return a random
            # movie, and ask the user to rate the movie
            # You should send the user the following information:
            # 1. Name of the movie
            # 2. A link to the movie on IMDB
            # TODO

            # Create a custom keyboard to let user enter rating
            my_inline_keyboard = [[
                InlineKeyboardButton(text='1', callback_data='rate_movie_1'),
                InlineKeyboardButton(text='2', callback_data='rate_movie_2'),
                InlineKeyboardButton(text='3', callback_data='rate_movie_3'),
                InlineKeyboardButton(text='4', callback_data='rate_movie_4'),
                InlineKeyboardButton(text='5', callback_data='rate_movie_5')
            ]]
            keyboard = InlineKeyboardMarkup(inline_keyboard=my_inline_keyboard )
            bot.sendMessage(chat_id, "How do you rate this movie?", reply_markup=keyboard)
        
        elif message == "/recommend":
            # Ask the server to generate a list of
            # recommended movies to the user
            # TODO
            bot.sendMessage(chat_id, "My recommendations:")

        else:
            # Some command that we don't understand
            bot.sendMessage(chat_id, "I don't understand your command.")

    elif content_type == "data":
        # This is data returned by the custom keyboard
        # Extract the movie ID and the rating from the data
        # and then send this to the server
        # TODO
        logging.info("Received rating: {}".format(data))
        bot.sendMessage(chat_id, "Your rating is received!")


if __name__ == "__main__":
    
    # Povide your bot's token 
    bot = telepot.Bot("__YOUR_TELEGRAM_BOT_TOKEN_HERE__")
    MessageLoop(bot, handle).run_as_thread()

    while True:
        time.sleep(10)
