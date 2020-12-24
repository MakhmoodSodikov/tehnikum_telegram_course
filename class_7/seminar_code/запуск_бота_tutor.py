from telegram.ext import Updater, CommandHandler  # Подключение нужных функций из модуля telegram

def start (update, context):
    name = update.message.from_user.first_name
    context.bot.send_message(chat_id=update.message.chat_id, text='Здарова ' + name + ', пыхнем?)')
def bye (update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text = 'Пока - пока)')



TOKEN = 'Фиг вам, а не мой токен)'

updater = Updater(token=TOKEN)  # Создаём переменную типа (Updater) с аргументом token, который равен переменной TOKEN

dispatcher = updater.dispatcher # Создаём диспетчер, который будет хранить все Handler'ы.

dispatcher.add_handler(CommandHandler('start', start))

dispatcher.add_handler(CommandHandler('bye', bye))

updater.start_polling(clean=True)  # Запуск работы бота.
updater.idle()  # Для завершения работы.