from telegram.ext import CommandHandler, Updater
import time
import telegram

def start(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id,
                                 action=telegram.ChatAction.TYPING)
    time.sleep(3)
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Salam Alekum')
    print(update.message.from_user.first_name)

    time.sleep(15)
    context.bot.send_chat_action(chat_id=update.message.chat_id,
                                 action=telegram.ChatAction.TYPING)
    time.sleep(3)
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Доброго времени суток')

TOKEN = ''

# Для асинхронной работы бота мы указываем в updater примерное кол-во пользователей одновременно.
updater = Updater(token=TOKEN, workers=20)

dispatcher = updater.dispatcher

# Для хендлеров, которые запускают функции, подразумеваюшие действия с паузами или длинными вевями кода - мы добавляем run_async=True, например
dispatcher.add_handler(CommandHandler('start', start, run_async=True))

updater.start_polling(clean=True)
updater.idle()