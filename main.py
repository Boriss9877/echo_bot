import telebot
from telebot import types
import API


bot = telebot.TeleBot(API.bot_API)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton('Включить повторяйку')
    markup.add(item)
    bot.send_message(
        message.chat.id, 'Это бот с повторяйкой, пока молчи', reply_markup=markup)


@bot.message_handler(content_types='text')
def text(message):

    if message.text == 'Включить повторяйку':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton('Выключить повторяйку')
        markup.add(item)
        bot.send_message(
            message.chat.id, 'Повторяйка включена, скажи что нибуть', reply_markup=markup)
        API.on_off = True

    elif message.text == 'Выключить повторяйку':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton('Включить повторяйку')
        markup.add(item)
        bot.send_message(
            message.chat.id, 'Повторяйка выключена, лучше молчи', reply_markup=markup)
        API.on_off = False

    elif API.on_off == True:
        bot.send_message(message.chat.id, message.text)

    else:
        bot.send_message(message.chat.id, 'Сказал же молчи мразь!!!!')


bot.infinity_polling()
