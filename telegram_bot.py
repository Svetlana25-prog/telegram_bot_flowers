import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKET = '7940519871:AAG_AMPSSV4l1a-ciuuejR4MGf8uFTCMuiE'
bot = telebot.TeleBot(TOKET)


def menu():
    row = ReplyKeyboardMarkup(resize_keyboard=True)
    row.add(KeyboardButton('📅 Узнать дату цветения'))
    row.add(KeyboardButton('➕ Добавить цветок'))
    return row

@bot.message_handler(commands=['start'])
def send_welcome(message):
    #bot.reply_to(message, 'Добро пожаловать!')
    bot.send_message(message.chat.id, 'Добро пожаловать!',reply_markup=menu())

@bot.message_handler(func=lambda message: message.text == '📅 Узнать дату цветения')
def ask_name_flowers(message):
    bot.send_message(message.chat.id, 'Введите название цветка: ')



@bot.message_handler(func=lambda message: True)
def send_flower_data(message):
    flowers = {}
    with open('date.txt', 'r', encoding='utf-8') as f:
        fl = f.read().split('\n')
        for line in fl:
            k = line.split(' - ')
            flowers[k[0]] = k[1]
    data = message.text.lower()
    fl = data.split(':')
    if fl[0] in flowers:
        bot.send_message(message.chat.id, f'Цветение {flowers[fl[0]]}')
    else:
        with open('date.txt', 'a', encoding='utf-8') as f:
            f.write(f'\n{fl[0]} - {fl[1]}')
        bot.send_message(message.chat.id, 'Такого цветка нет, но он уже добавлен')



bot.polling()