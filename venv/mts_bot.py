import telebot
import requests
import json
import time
import urllib
from telebot import types
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, User, Message, Update, Chat, ChatMember, UserProfilePhotos, File, ReplyMarkup, TelegramObject, WebhookInfo, GameHighScore, StickerSet, PhotoSize, Audio, Document, Sticker, Video, Animation, Voice, VideoNote, Location, Venue, Contact, InputFile, Poll, BotCommand
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

phone = ''

def get_answer_rko(bot, update):
    f = open('result.txt', 'a')
    f.write(str(bot.message.chat.id) + " " + str(bot.message.chat.username) + " " + str(bot.message.contact.phone_number) +"\n")
    f.close()
    bot.message.reply_text('Для того, что бы оставить заявку на РКО и получить по ней решение '

                           'достаточно написать ИНН (на который будет открыт РКО), серию/номер паспорта и дату рождения', reply_markup=ReplyKeyboardRemove())


def sms(bot, update):
    request_rko = ReplyKeyboardMarkup([[KeyboardButton('Хочу открыть РКО для ИП', request_contact=True)],
                                       [KeyboardButton('Хочу открыть РКО для ЮЛ', request_contact=True)]], resize_keyboard=True)
    bot.message.reply_text('Здравствуйте! Вы хотите открыть РКО?', reply_markup=request_rko)

def get_message(bot, update):
    f = open('result.txt', 'a')
    f.write(str(bot.message.chat.id) + " " + str(
        bot.message.chat.username) + " " + str(bot.message.chat.first_name) + " " + str(bot.message.chat.last_name) + " " + str(bot.message.text) + "\n")
    f.close()
    bot.message.reply_text('Если вы указали верные данные, то скоро мы скоро с вами свяжемся! Если вы хотите оставить еще одну заявку введите /start', reply_markup = ReplyKeyboardRemove())

def main():
    m_bot = Updater('733808783:AAExrBP4PFYg3ZQJbCMaLSIG28NMcBVObZ0', 'https://telegg.ru/orig/bot', use_context=True)
    m_bot.dispatcher.add_handler(CommandHandler('start', sms))
    m_bot.dispatcher.add_handler(MessageHandler(Filters.contact, get_answer_rko))
    m_bot.dispatcher.add_handler(MessageHandler(Filters.text, get_message))
    m_bot.start_polling()
    m_bot.idle()

main()
