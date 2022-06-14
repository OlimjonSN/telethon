import telebot
import time
from time import time
bot = telebot.TeleBot('1435916631:AAHfsRoid_8KRAK8t72bc1Gsy4MSlEnKjus')
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(content_types= 'text')
def echo_all(message):
	bot.restrict_chat_member(message.chat.id, message.from_user.id, until_date=time() + 60)

bot.infinity_polling()