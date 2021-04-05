"""
Модуль для старта проекта
"""
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters
from const import API_TOKEN
from functions import *

updater = Updater(token=API_TOKEN, workers=20)

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start',
                                      start, run_async=True))

dispatcher.add_handler(MessageHandler(Filters.text,
                                      text_msg, run_async=True))

dispatcher.add_handler(MessageHandler(Filters.contact,
                                      get_contact))

dispatcher.add_handler(MessageHandler(Filters.location,
                                      get_location))

dispatcher.add_handler(CallbackQueryHandler(callback=inline_reply,
                                            pattern='yes'))

dispatcher.add_handler(MessageHandler(Filters.photo,
                                      photo_msg))


updater.start_polling()

updater.idle()
