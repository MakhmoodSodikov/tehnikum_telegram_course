"""
Модуль для функций
"""
import messege as msg
import answers as ans


def start(update, context):
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    text = msg.start_text.format(first_name)
    context.bot.send_message(chat_id=chat_id, text=text)


def text_msg(update, context):
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    text = update.message.text.lower()

    send_text = ans.global_answers['rus'][text]

    context.bot.send_message(chat_id=chat_id,text=send_text)
