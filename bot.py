import telebot
from selenium import webdriver
import re

from screener import DIR_PATH, run_screener
import _config


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
	# getting screenshot at sending it back to user
	run_screener(message.text)
	with open(f"{DIR_PATH}/static/screenshot_.png", 'rb') as image_file:
		bot.send_photo(message.chat.id, image_file, 'caption')


# other messages => instructions
@bot.message_handler(func=lambda msg: True)
def handle_message(message):
	bot.reply_to(message, 'Send me URL, please.')


if __name__ == '__main__':
    bot.polling(none_stop=True)
