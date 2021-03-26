"""
Модуль для функций
"""
import time
import messege as msg
import answers as ans
import markup as mrk
from telegram.constants import CHATACTION_TYPING

def start(update, context):
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    text = msg.start_text.format(first_name)
    context.bot.send_message(chat_id=chat_id, text=text)


def text_msg(update, context):
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    text = update.message.text.lower()
    if text == 'показать инлайн кнопки':
        context.bot.send_message(chat_id=chat_id,
                                 reply_markup=mrk.inline_button(),
                                 text='Кнопка нажата! Выберите ниже другую')
    else:
        send_text = ans.global_answers['rus'][text]
        context.bot.send_message(chat_id=chat_id,
                                 text=send_text,
                                 reply_markup=mrk.button())


def inline_reply(update, context):
    chat_id = update.callback_query.from_user.id
    message_id = update.callback_query.message.message_id
    first_name = update.callback_query.from_user.first_name
    context.bot.send_chat_action(chat_id=chat_id, action=CHATACTION_TYPING)
    context.bot.delete_message(chat_id=chat_id, message_id=message_id)
    time.sleep(2.5)
    context.bot.send_message(chat_id=chat_id, text="okey")

