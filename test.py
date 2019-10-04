import telebot

bot_token = '947391023:AAHvrZui6RmAngetinFaJProC7p4V7_twac'
bot = telebot.TeleBot(token=bot_token) 

# BOT - START
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message("871164939","ES UM GANDA BURRO !")

bot.polling()