import datetime
import time
import messages as msg
import answers_dicts as ans
from sms import send_sms
from spell import Spell
import markups as mrk
from telegram.constants import CHATACTION_TYPING
import sqlite3
from const import DB_PATH
from telegram import ReplyKeyboardRemove
import db_requests as req
from utils import execute_request
import random


def start(update, context):
    # chat_id = update.message.chat_id
    # time.sleep(15)
    # context.bot.send_message(chat_id=chat_id,
    #                          text='hi')
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    username = update.message.chat.username

    text = msg.start_text.format(first_name)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    val = cursor.execute('''
        SELECT id
        FROM users
        WHERE id = '{}'
        LIMIT 1
    '''.format(chat_id)).fetchone()

    if val is None:
        code = random.randint(1000, 9999)
        cursor.execute('''
        INSERT INTO users (id, username, stage) VALUES('{}', '{}', '{}')
        '''.format(chat_id, username, code))

        conn.commit()

    context.bot.send_message(chat_id=chat_id,
                             reply_markup=mrk.get_phone(),
                             text=text)


def text_msg(update, context):
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    text = update.message.text.lower()
    message_id = update.message.message_id

    context.bot.send_message(chat_id=chat_id,
                             text='another hi')

    # if text == 'показать инлайн-кнопки':
    #     context.bot.send_message(chat_id=chat_id,
    #                              reply_markup=mrk.inline_button(),
    #                              text='Кнопка нажата! Выберите ниже другую:')
    # elif :
    #     send_text = ans.global_answers['rus'][text]
    #     context.bot.send_message(chat_id=chat_id,
    #                              text=send_text,
    #                              reply_markup=mrk.button())

    if len(text) == 12 and text[:3] == '998' and text.isdigit():
        phone = int(text)

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute('''
            UPDATE users
            SET phone = '{}'
            WHERE id = '{}'
            '''.format(phone, chat_id))

        conn.commit()

        context.bot.send_message(chat_id=chat_id,
                                 reply_markup=mrk.start_order(),
                                 text=msg.start_order)

    if text == 'начать заказ':
        print(1)
        context.bot.edit_message_reply_markup(chat_id=chat_id,
                                              message_id=message_id - 1,
                                              reply_markup=None)


def inline_reply(update, context):
    chat_id = update.callback_query.from_user.id
    message_id = update.callback_query.message.message_id
    first_name = update.callback_query.from_user.first_name

    context.bot.send_chat_action(chat_id=chat_id,
                                 action=CHATACTION_TYPING)

    context.bot.delete_message(chat_id=chat_id,
                               message_id=message_id)

    context.bot.send_message(chat_id=chat_id,
                             text='Окей')


def photo_msg(update, context):
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    photo_id = update.message.photo[-1].file_id
    print(chat_id)
    f = context.bot.get_file(photo_id)
    print(f)
    t = datetime.datetime.now().second
    print(update.message.chat.id)
    f.download('photos/{}.jpg'.format(str(chat_id)))


def get_contact(update, context):
    chat_id = update.message.chat_id
    phone = update.message.contact.phone_number
    phone = int(phone)
    print(phone)


    execute_request(req.UPDATE_PHONE.format(phone, chat_id))
    
    context.bot.send_message(chat_id=chat_id,
                             reply_markup=mrk.start_order(),
                             text=msg.start_order)
    code = execute_request(req.SELECT_CODE.format(chat_id))[0][0]
    print(code)
    print(send_sms(phone, code))


def get_location(update, context):
    loc = update.message.location
    print(loc)
