from datetime import datetime
import telebot
import json
from Tests import NetworkSpeedTest, Screenshot, UserInfoTest
import time

# config settings
config = json.load(open("config.json"))
bot = telebot.TeleBot(config['token'], parse_mode="Markdown")


def scheduler(beginTimer):
    animation = ['-', '\\', '|', '/', '-', '\\', '|', '/', '-']
    animationIndex = 0
    messageText = ("``` New job has been started at {}. Working ... {}\n" + " - [ ] {}\n" * len(config['tasks']) + "```")
    startMessage = bot.send_message(chat_id=config['userSession'],
                                    text=messageText.format(beginTimer, animation[animationIndex], *config['tasks']))
    while True:
        time.sleep(1)
        bot.edit_message_text(chat_id=config['userSession'],
                              message_id=startMessage.message_id,
                              text=messageText.format(beginTimer, animation[animationIndex+1], *config['tasks']))
        if animationIndex < len(animation) - 2:
            animationIndex += 1
        else:
            animationIndex = 0


scheduler(str(datetime.now())[:-7])
exit()

starts = datetime.now()

client = UserInfoTest.getUserInfo()
network = NetworkSpeedTest.calculate()

for header in client.keys():
    bot.send_message(chat_id=config['userSession'], text="{} - {}".format(header, client[header]))
    
for header in network:
    bot.send_message(chat_id=config['userSession'], text="{} - {}".format(header, network[header]))
    

'''
try:
    Screenshot.makeScreenshot()
    1 // 0
except Exception:
    print("Attempt to make screenshot failed")
'''

ends = datetime.now()
workSpeedTest = ends - starts
bot.send_message(chat_id=config['userSession'], text="It took for {} to complete task".format(workSpeedTest))
bot.send_message(chat_id=config['userSession'], text='-'*10)
