
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        for i in footer_buttons:
            menu.append([i])
    return menu


def nyka():
    button_list = [
            InlineKeyboardButton("Узнать мнение других!", callback_data='yes'),
    ]
    return InlineKeyboardMarkup(build_menu(button_list, 1))


button_list = [
        KeyboardButton("Узнать мнение других!", callback_data='yes'),
    ]
reply_markup=ReplyKeyboardMarkup([button_list])
# ------------------------------------------------------------


bot.send_message(chat_id=user_id,
                 text=msg.wait_a_min,
                 reply_markup=mrk.nyka(),
                 parse_mode=telegram.ParseMode.MARKDOWN)

# ------------------------------------------------------------

import pickle
mylist = ['a', 'b', 'c', 'd']
with open('datafile.txt', 'wb') as fh:
   pickle.dump(mylist, fh)
  
pickle_off = open ("datafile.txt", "rb")
emp = pickle.load(pickle_off)
print(emp)

# ------------------------------------------------------------

from telegram.ext.dispatcher import run_async

updater = Updater(token=const.TOKEN_TELEGRAM_BOT, workers=20)


# ------------------------------------------------------------

file = bot.getFile(update.message.photo[-1].file_id)
file.download('photo_db/new_photos_{}.jpg'.format(user_id))


# ------------------------------------------------------------

def get_file(update, context):
    file = context.bot.getFile(update.message.voice.file_id)
    file.download('voice.mp3'.format(update.message.from_user.id))
    context.bot.send_message(chat_id=update.message.from_user.id,
                             text='good',
                             parse_mode=telegram.ParseMode.MARKDOWN)
                             
# ------------------------------------------------------------   


bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
