from postgresminrec import *
from telebot import *
from service import *
from emailservice import *

bot = telebot.TeleBot("6134182063:AAFu9mpxZ5JFVgsbRH0X8sx4isnQN93GfvY")

info = "Наши контакты\n" \
       "😎🤙🏻👋🏻🤝🏻\n\n" \
       "☎   телефон- +7-916-157-11-31\n " \
       "👔   Вероника\n" \
       "✉   email - romanze1706@gmail.com"

opportunities = "<em>Наши возможности</em> \n" \
                "🎧💿🎙️🎹\n\n" \
                "🎼<b>  Аранжировка</b>\n" \
                "🔊<b>  Сведение</b>\n" \
                "💽<b>  Мастеринг</b>\n" \
                "🎤<b>  Обработка вокала</b>\n" \
                "🎸<b>  Написание партий гитары/бас-гитары</b>\n"


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
                   "😐👉🚪   <em> Добро пожаловать в домашнюю студию звукозаписи</em>\n"
                   "🖐 🙌 👋🏼 🔊 🔥\n"
                   "🎤📀💻 <b>MinimalRecords</b>\n\n" + opportunities, parse_mode='html',
                   reply_markup=get_replay_keyboard(message))


def get_replay_keyboard(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("🌍 Наш сайт", web_app=types.WebAppInfo("https://roma17111.github.io/index.html"))
    btn1 = types.KeyboardButton("📱 Заказать услугу")
    if is_user_admin(message.chat.id):
        markup.row(types.KeyboardButton("🧑🏻‍💻 Список пользователей"), types.KeyboardButton("🧰 Список заявок"))
    markup.row(types.KeyboardButton("📣 Наши возможности"), btn1)
    markup.row(btn, types.KeyboardButton("🗨️ Контакты"))
    return markup


@bot.message_handler()
def main(message):
    if message.text == "🧑🏻‍💻 Список пользователей":
        bot.send_message(message.chat.id, get_all_users())
    elif message.text == "📱 Заказать услугу":
        bot.send_message(message.chat.id, "🤝  Представьтесь")
        bot.register_next_step_handler(message, get_fio)
    elif message.text == "🗨️ Контакты":
        bot.send_message(message.chat.id, info)
    elif message.text == "📣 Наши возможности":
        bot.send_message(message.chat.id, opportunities, parse_mode='html')
    elif message.text == "🧰 Список заявок":
        bot.send_message(message.chat.id, get_all_services())
    else:
        bot.send_message(message.chat.id, "⚙️  Выберите действие ", reply_markup=get_replay_keyboard(message))


def get_fio(message):
    try:
        fio = message.text.strip()
        bot.send_message(message.chat.id, "☎️  Укажите телефон")
        bot.register_next_step_handler(message, get_phone, fio)
    except AttributeError:
        bot.send_message(message.chat.id, "❌❗⚠️ Введите только текст\n\n"
                                          "👩🏻‍💻 Представьтесь")
        bot.register_next_step_handler(message, get_fio)


def get_phone(message, fio):
    try:
        phone = message.text.strip()
        bot.send_message(message.chat.id, "📧  Укажите email")
        bot.register_next_step_handler(message, get_email, fio, phone)
    except AttributeError:
        bot.send_message(message.chat.id, "❌❗⚠️ Введите только текст\n\n"
                                          "☎️  Укажите телефон")
        bot.register_next_step_handler(message, get_phone, fio)


def get_email(message, fio, phone):
    try:
        email = message.text.strip()
        bot.send_message(message.chat.id, "🧾  Опишите услугу")
        bot.register_next_step_handler(message, get_description, fio, phone, email)
    except AttributeError:
        bot.send_message(message.chat.id, "❌❗⚠️ Введите только текст\n\n"
                                          "📧  Введите email")
        bot.register_next_step_handler(message, get_email, fio, phone)


def get_description(message, fio, phone, email):
    try:
        description = message.text.strip()
        bot.send_message(message.chat.id, "✔️  Заявка на оказание услуги отправлена\n"
                                          "👍  с вами свяжутся в ближайшее время",
                         reply_markup=get_replay_keyboard(message))
        serv = Service(message.chat.id, fio, phone, email, description)
        s = str(serv.get_info())
        bot.send_message(message.chat.id, s)
        send_email(s)
        create_service(fio, phone, email, description)
    except AttributeError:
        bot.send_message(message.chat.id, "Введите только текст\n\n"
                                          "Опишите услугу")
        bot.register_next_step_handler(message, get_description, fio, phone, email)


def get_site(message):
    markup = types.InlineKeyboardMarkup()
    site = types.InlineKeyboardButton("тык", url="https://roma17111.github.io/index.html")
    markup.row(site)
    bot.send_message(message.chat.id, "Перейти на сайт", reply_markup=markup)


@bot.message_handler(content_types=['photo', 'audio', 'video'])
def other(message):
    bot.reply_to(message, "🔥😊👍 Супер")
    bot.send_message(message.chat.id, "⚙️  Выберите действие ", reply_markup=get_replay_keyboard(message))


bot.polling(none_stop=True)
