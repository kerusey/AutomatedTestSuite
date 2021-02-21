from telebot import TeleBot

app = TeleBot(__name__)
app.config['api_key'] = '1607134909:AAHQbKK4SG5ynNYjaWp8h5KJg3s8fqK1C9A'
chat_dest = 331774665
app.send_message(chat_dest, "")


