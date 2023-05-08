from telebot import *

bot = TeleBot("6134182063:AAFu9mpxZ5JFVgsbRH0X8sx4isnQN93GfvY")


@bot.message_handler()
def main(message):
    bot.send_message(message.chat.id, "Вы ввели -" + message.text)


bot.polling(none_stop=True)
