from postgresminrec import *
from telebot import *
from service import *
from emailservice import *

bot = telebot.TeleBot("6134182063:AAFu9mpxZ5JFVgsbRH0X8sx4isnQN93GfvY")


@bot.message_handler(commands=["start"])
def main(message):
    if len(get_user_by_chat_id(message.chat.id)) == 0:
        register_user(message.chat.id,
                      message.chat.first_name,
                      message.chat.last_name,
                      message.chat.username)

    file = open("./Minrec.jpg", "rb")
    bot.send_photo(message.chat.id, file,
                   message.chat.first_name + "." +
                   "<em> Добро пожаловать в домашнюю студию звукозаписи</em>\n"
                   "<b>MinimalRecords</b>", parse_mode='html', reply_markup=get_replay_keyboard())


def get_replay_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Наш сайт", web_app=types.WebAppInfo("https://roma17111.github.io/index.html"))
    btn1 = types.KeyboardButton("Список пользователей")
    markup.row(btn, types.KeyboardButton("Заказать услугу"))
    markup.row(btn1)
    return markup


@bot.message_handler()
def main(message):
    if message.text == "Список пользователей":
        bot.send_message(message.chat.id, get_all_users())
    elif message.text == "Заказать услугу":
        bot.send_message(message.chat.id, "Представьтесь")
        bot.register_next_step_handler(message, get_fio)
    else:
        bot.send_message(message.chat.id, "Вы ввели - " + message.text, )


def get_fio(message):
    fio = message.text.strip()
    bot.send_message(message.chat.id, "Укажите телефон")
    bot.register_next_step_handler(message, get_phone, fio)


def get_phone(message, fio):
    phone = message.text.strip()
    bot.send_message(message.chat.id, "Укажите email")
    bot.register_next_step_handler(message, get_email, fio, phone)


def get_email(message, fio, phone):
    email = message.text.strip()
    bot.send_message(message.chat.id, "Опишите услугу")
    bot.register_next_step_handler(message, get_description, fio, phone, email)


def get_description(message, fio, phone, email):
    description = message.text.strip()
    bot.send_message(message.chat.id, "Заявка на оказание услуги отправлена\n"
                                      "с вами свяжутся в ближайшее время", reply_markup=get_replay_keyboard())
    serv = Service(message.chat.id, fio, phone, email, description)
    s = str(serv.get_info())
    bot.send_message(message.chat.id, s)
    send_email(s)


def get_site(message):
    markup = types.InlineKeyboardMarkup()
    site = types.InlineKeyboardButton("тык", url="https://roma17111.github.io/index.html")
    markup.row(site)
    bot.send_message(message.chat.id, "Перейти на сайт", reply_markup=markup)


bot.polling(none_stop=True)
