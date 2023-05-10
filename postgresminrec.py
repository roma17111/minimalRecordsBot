import psycopg2
from psycopg2 import Error


def get_all_users():
    connection = psycopg2.connect(user="user",
                                  # пароль, который указали при установке PostgreSQL
                                  password="12345",
                                  host="asha.webtm.ru",
                                  port="5432",
                                  database="minrec")
    with connection.cursor() as cursor:
        cursor.execute("select * from users")
        users = cursor.fetchall()
        print(len(users))
        info = "Список пользователей\n\n"
        for el in users:
            info += f'🌐  Ник:  @{el[2]}\n  🤵  Имя:  {el[3]}\n 🧍🏽  Фамилия:  {el[4]}\n ID  {el[1]}\n'
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")
    return info


def register_user(chat_id, first_name, last_name, nick_name):
    connection = psycopg2.connect(user="user",
                                  # пароль, который указали при установке PostgreSQL
                                  password="12345",
                                  host="asha.webtm.ru",
                                  port="5432",
                                  database="minrec")
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO users (chat_id,first_name,last_name,nick_name,is_admin)"
                       " VALUES ('%d', '%s', '%s', '%s', false)" % (
                           chat_id, first_name, last_name, nick_name))
        print("Пользователь зарегистрирован!")
        connection.commit()
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")


def get_user_by_chat_id(chat_id):
    connection = psycopg2.connect(user="user",
                                  # пароль, который указали при установке PostgreSQL
                                  password="12345",
                                  host="asha.webtm.ru",
                                  port="5432",
                                  database="minrec")
    with connection.cursor() as cursor:
        cursor.execute(f"select * from users where chat_id = '%d'" % chat_id)
        print("Пользователь зарегистрирован!")
        c = cursor.fetchall()
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")
    return c


def create_service(fio, phone, email, description):
    connection = psycopg2.connect(user="user",
                                  # пароль, который указали при установке PostgreSQL
                                  password="12345",
                                  host="asha.webtm.ru",
                                  port="5432",
                                  database="minrec")
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO service (fio, phone, email, description)"
                       " VALUES ('%s', '%s', '%s', '%s')" % (
                           fio, phone, email, description))
        print("Заявка оформлена!")
        connection.commit()
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")


def get_all_services():
    connection = psycopg2.connect(user="user",
                                  # пароль, который указали при установке PostgreSQL
                                  password="12345",
                                  host="asha.webtm.ru",
                                  port="5432",
                                  database="minrec")
    with connection.cursor() as cursor:
        cursor.execute("select * from service")
        s = cursor.fetchall()
        info = "Список заявок на оказание услуги\n\n"
        for el in s:
            info += f'🧑🏻 ФИО:  {el[1]}\n  📱  Телефон:  {el[2]}\n ' \
                    f'📧  email:  {el[3]}\n 📑  описание услуги: {el[4]} \n'
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")
    return info


def is_user_admin(chat_id):
    connection = psycopg2.connect(user="user",
                                  # пароль, который указали при установке PostgreSQL
                                  password="12345",
                                  host="asha.webtm.ru",
                                  port="5432",
                                  database="minrec")
    with connection.cursor() as cursor:
        cursor.execute(f"select * from users where chat_id = '%d' and is_admin = true" % chat_id)
        print("Пользователь зарегистрирован!")
        c = cursor.fetchall()
        if len(c) == 0:
            return False
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")
    return True
