import telebot
from selenium import webdriver
import re
import os

from screener import run_screener
import _config


DIR_PATH = os.getcwd() + "/static"
RE_URL = r'((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)'


# bot init
bot = telebot.TeleBot(_config.TOKEN)
print("Bot running ...")


# '/start' => hi message
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Welcome! Please, send me your URL and I'll give you a screenshot.")


# URL REGEXP => screenshot
@bot.message_handler(regexp=RE_URL)
def handle_message(message):
	# getting screenshot and sending it back to user
	bot.reply_to(message, "Please, wait. I am getting web page screenshot ...")
	run_screener(message.text)
	with open(f"{DIR_PATH}/screenshot.png", 'rb') as image_file:
		print("Bot preparing to sending screenshot ...")
		bot.send_document(message.chat.id, image_file)
		print("Screenshot sent to client!")
		

# other messages => instructions
@bot.message_handler(func=lambda msg: True)
def handle_message(message):
	bot.reply_to(message, 'Send me URL, please.')


if __name__ == '__main__':
    bot.polling(none_stop=True)
