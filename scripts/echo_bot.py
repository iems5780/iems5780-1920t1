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
    
    # Povide your bot's token 
    bot = telepot.Bot("624591791:AAFAC7bObeMdq-ZTjGOD0RiyeTX7ObSQvsk")
    MessageLoop(bot, handle).run_as_thread()

    while True:
        time.sleep(10)
