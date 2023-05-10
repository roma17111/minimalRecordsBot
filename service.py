class Service:
    chat_id = None
    full_name = None
    phone_number = None
    email = None
    description = None

    def __init__(self, chat_id=None, full_name=None, phone_number=None, email=None, description=None):
        self.chat_id = chat_id
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.description = description

    def get_info(self):
        s = "📖  Ваша заявка:\n Чат ID " + str(self.chat_id) + '\n' + "😎  ФИО\n" + self.full_name +\
            "\n☎️  Номер телефона \n" + self.phone_number + '\n' + "📧  email\n" + self.email + \
            "\n📋  Описание услуги\n" + self.description
        return s
