import telebot
#import requests
 
from telebot import types
 
bot_token = '947391023:AAHvrZui6RmAngetinFaJProC7p4V7_twac'
bot = telebot.TeleBot(token=bot_token)
 
markup = types.ReplyKeyboardRemove(selective=False)

# BOT - COMANDO ERROR
@bot.message_handler(func=lambda message: True)
def send_error(message):
    chatid = message.chat.id
    bot.send_message(chatid,"Comando Inesxistente, se precisares de ajudar faz: /help")

# BOT - START
@bot.message_handler(commands=['start'])
def send_welcome(message):    
    chatid = message.chat.id
    bot.send_message(chatid,"Hello World, im @GreenBookTipsBot")
 
# BOT - HELP
@bot.message_handler(commands=['help'])
def send_help(message):
    chatid = message.chat.id
    bot.send_message(chatid,"Help in: ")
 
# BOT - ADERIR 
@bot.message_handler(commands=['menu'])
def show_menu(message):
    chatid = message.chat.id
    markup_menu = types.ReplyKeyboardMarkup(row_width=4)
    button1 = types.KeyboardButton('Button 1',)
    button2 = types.KeyboardButton('Button 2')
    button3 = types.KeyboardButton('Button 3')
    button4 = types.KeyboardButton('Button 4')
    markup_menu.add(button1, button2, button3, button4)
    bot.send_message(chatid, "Choose one option from the menu", reply_markup=markup_menu)
 
@bot.message_handler(func=lambda msg: msg.text is not None and 'Button 1' in msg.text)
def echo(message):
    chatid = message.chat.id
    bot.send_message(chatid,"You just clicked on mes 1", reply_markup=markup)
    nome = bot.send_message(chatid,"Escolha 1/2/3 ")
    bot.register_next_step_handler(nome, aderir_grupo)
 
def aderir_grupo(message):
    chatid = message.chat.id
    aderir = int(message.text)
    if aderir == 1:
        bot.send_message(chatid, "Escolheste o 1")
    elif aderir == 2:
        bot.send_message(chatid, "Escolheste o 2")
    elif aderir == 3:
        bot.send_message(chatid, "Escolheste o 3")
    else:
        bot.send_message(chatid, "Escolheste uma operacao invalida")
 
bot.polling()