import telebot
from selenium import webdriver

import screener
import _config


# bot init
bot = telebot.TeleBot(_config.TOKEN)


# Hi responce message
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Welcome! Send me URL pleace.")


# later will replace 'func=lambda msg: True' on URL regex filter - 'regexp="SOME_REGEXP" '
@bot.message_handler(func=lambda msg: True)
def echo_message(message):
	bot.reply_to(message, screener.checkScreenshot())


# @bot.message_handler(func=lambda msg: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)


print("Bot running ...")
bot.polling(none_stop=True)
