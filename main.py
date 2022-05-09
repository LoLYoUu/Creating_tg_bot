import telebot
from telebot import types

token = '5226575443:AAE0O0pnxTOObtPeKk4JjgzAMJgsd2URS2c'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/привет", "/help", "/пока")
    keyboard.row("Хочу", "МТУСИ?", "Сколько лет?", "Спасибо!")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


@bot.message_handler(commands=['привет'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/привет", "/help", "/пока")
    keyboard.row("Хочу", "МТУСИ?", "Сколько лет?", "Спасибо!")
    bot.send_message(message.chat.id, 'Привет! Я бот, умею много интересного. Напиши мне /help, чтобы узнать, что я умею!', reply_markup=keyboard)



@bot.message_handler(commands=['пока'])
def start(message):
    bot.send_message(message.chat.id, 'До встречи! Надеюсь, еще увидимся!')


@bot.message_handler(commands=['help'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/привет", "/help", "/пока")
    keyboard.row("Хочу", "МТУСИ?", "Сколько лет?", "Спасибо!")
    bot.send_message(message.chat.id, 'Все очень просто!\nВот команды которые я знаю:')
    bot.send_message(message.chat.id, '/привет - Мы поздороваемся)\n/пока - мы попорощаемся))\n/help - ты уже про нее знаешь, тут я расскажу что я умею')
    bot.send_message(message.chat.id, 'А вот что ты мне можешь сказать:')
    bot.send_message(message.chat.id, '\"Хочу\" - расскажу как поступить к нам\n\"МТУСИ?\" - поясню за расшифровку\n\"Сколько лет\" - расскажу сколько нам лет и нашу историю', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    elif message.text.lower() == "мтуси?":
        bot.send_message(message.chat.id, 'Аббревиатура \"МТУСИ\" расшифровывается как\n \"Московский Технический Университет Связи и Информатики\"')
    elif message.text.lower() == "сколько лет?":
        bot.send_message(message.chat.id, 'Нашему университету 101 год!\nОн был основан в 1921 году постановлением Главного Управления профессионального образования и коллегии Народного Комиссариата почт и телеграфов')
    elif message.text.lower() == "спасибо!":
        bot.send_message(message.chat.id, 'Пожалуйста!\nБыло приятно рассказать о нашем университете!')


bot.polling(none_stop=True, interval=0)

