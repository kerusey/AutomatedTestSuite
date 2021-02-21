from datetime import datetime
import telebot
import json
from Tests import NetworkSpeedTest, Screenshot, UserInfoTest

# config settings
config = json.load(open("config.json"))
app = telebot.TeleBot(__name__)
app.config['api_key'] = config['token']
chatID = config['userSession']

starts = datetime.now()

app.send_message(chatID, "New job has been started at {}".format(datetime.now()))
app.send_message(chatID, "-"*10)

client = UserInfoTest.getUserInfo()
network = NetworkSpeedTest.calculate()

for header in client.keys():
    app.send_message(chatID, "{} - {}".format(header, client[header]))
    
for header in network:
    app.send_message(chatID, "{} - {}".format(header, network[header]))
    

'''
try:
    Screenshot.makeScreenshot()
    1 // 0
except Exception:
    print("Attempt to make screenshot failed")
'''

ends = datetime.now()
workSpeedTest = ends - starts
app.send_message(chatID, "It took for {} to complete task".format(workSpeedTest))
app.send_message(chatID, '-'*10)
