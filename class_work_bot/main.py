"""
Модуль для старта проекта
"""




from const import API_TOKEN
from function import *


updater = Updater(token=API_TOKEN)

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))

dispatcher.add_handler(MessageHandler(Filters.text, text_msg))

updater.start_polling()
