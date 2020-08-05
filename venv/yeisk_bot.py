import telebot
import requests
import json
import time
import urllib
from telebot import types
import re
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, User, Message, Update, Chat, ChatMember, UserProfilePhotos, File, ReplyMarkup, TelegramObject, WebhookInfo, GameHighScore, StickerSet, PhotoSize, Audio, Document, Sticker, Video, Animation, Voice, VideoNote, Location, Venue, Contact, InputFile, Poll, BotCommand
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

url = 'http://127.0.0.1:8000/index/'

def get_answer_rko(bot, update):
    bot.message.reply_text('Для того, что бы оставить заявку на РКО и получить по ней решение '

                           'достаточно написать ИНН (на который будет открыт РКО), серию/номер паспорта и дату рождения', reply_markup=ReplyKeyboardRemove())


def sms(bot, update):
    request_rko = ReplyKeyboardMarkup([[KeyboardButton('Хочу сделать заказ тут')],
                                       [KeyboardButton('Хочу получить больше информации')],
                                       [KeyboardButton('Хочу, что бы мне позвонил оператор', request_contact=True)]], resize_keyboard=True)
    bot.message.reply_text('Здравствуйте! Данный бот поможет вам сделать заказ на любые товары из магазинов вашего города.'
                           ' Вы хотите сделать заказ?', reply_markup=request_rko)

def get_message(bot, update):
    bot.message.reply_text('Отлично! Напишите, пожалуйста, что бы вы хотели заказать? Писать можно в '
                           'произвольной форме. Для корректной работы нужно написать контактный номер, по которому с вами свяжется оператор для подтверждения заказа.\n'
                           'Например: \n'
                           'сыр Эдам (до 100 рублей за упаковку),'
                           'пачку сигарет красный мальборо, сникерс большой. Доставить по адресу улица Ленина дом 15 в '
                           'ближайшее время. 89593412323', reply_markup = ReplyKeyboardRemove())

def more_info(bot, update):
    bot.message.reply_text('Дорогие друзья! Данный бот создан с едиснтвенной целью - помочь людям получить продукты и вещи в '
                           'максимально сжатые сроки. Сделать заказ очень просто одним из способов: \n'
                           '1) Использовать данного бота \n'
                           '2) Воспользоваться сайтом www.site.ru \n'
                           '3) Позвонить на горячую линию по телефону 8 888 888 88 88 \n'
                           'Мы будем рады помочь вам в любое время! Для того, что бы начать снова введите /start', reply_markup=ReplyKeyboardRemove())

def end_process(bot, update):
    requests.post(url, data={'tovar': str(bot.message.text) + " \n Необходимо позвонить клиенту", 'phone':'telegramm_bot', 'adress': 'telegramm_bot'})
    bot.message.reply_text('Ваш заказ принят! В ближайшее время с вами свяжется оператор для подтверждения заказа. Что бы начать снова введите /start', reply_markup=ReplyKeyboardRemove())

def want_to_call(bot, update):
    requests.post(url, data={'tovar': 'Необхоимо позвонить клиенту', 'phone': str(bot.message.contact.phone_number), 'adress': 'telegramm_bot'})
    bot.message.reply_text('Спасибо за ваш выбор! Мы свяжемся с вами в ближайшее время, по указанному вами телефону. Что бы начать снова введите /start', reply_markup=ReplyKeyboardRemove())

def main():
    m_bot = Updater('1331948903:AAER0uZ2fTENwWpyO1F_XgIJjXRSry8mY04', 'https://telegg.ru/orig/bot', use_context=True)
    m_bot.dispatcher.add_handler(CommandHandler('start', sms))
    m_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Хочу получить больше информации'), more_info))
    m_bot.dispatcher.add_handler(MessageHandler(Filters.contact, want_to_call))
    m_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Хочу сделать заказ тут'), get_message))
    m_bot.dispatcher.add_handler(MessageHandler(Filters.text, end_process))
    m_bot.start_polling()
    m_bot.idle()

main()
