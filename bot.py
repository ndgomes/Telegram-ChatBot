import telebot
import requests

#from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot_token = '947391023:AAHvrZui6RmAngetinFaJProC7p4V7_twac'
bot = telebot.TeleBot(token=bot_token) 

# BOT - START
@bot.message_handler(commands=['start'])
def send_welcome(message):    
    chatid = message.chat.id
    nome = message.chat.first_name
    bot.send_message(chatid, "Hey {}" .format(nome) + " !")
    btn1 = InlineKeyboardButton("Happy", callback_data='1')
    btn2 = InlineKeyboardButton("Whatever", callback_data='2')
    markup = InlineKeyboardMarkup(row_width=2)            
    markup.add(btn1,btn2)
    bot.send_message(chatid, "Hey There !", reply_markup=markup)

@bot.callback_query_handler(lambda query: query.data == "1")
def send_happy(query):
    chatid = query.chat.id
    bot.send_message(chatid, "hapy")

# BOT - HELP
@bot.message_handler(commands=['help'])
def send_help(message):
    chatid = message.chat.id
    bot.send_message(chatid,"Help in: ")

# BOT - ERROR
@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(message):
    chatid = message.chat.id
    bot.send_message(chatid, "/help")

bot.polling()