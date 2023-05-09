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
            info += f'Ник:  @{el[2]}  Имя:  {el[3]}  Фамилия:  {el[4]}\n'
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
        cursor.execute("INSERT INTO users (chat_id,first_name,last_name,nick_name)"
                       " VALUES ('%d', '%s', '%s', '%s')" % (
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
