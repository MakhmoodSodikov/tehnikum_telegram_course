"""
Модуль для старта проекта
"""
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler



from const import API_TOKEN
from function import *


updater = Updater(token=API_TOKEN)

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))

dispatcher.add_handler(MessageHandler(Filters.text, text_msg))

dispatcher.add_handler(CallbackQueryHandler(callback=inline_reply, pattern='yes'))

updater.start_polling()

updater.idle()
