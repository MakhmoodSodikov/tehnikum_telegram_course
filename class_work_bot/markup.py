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


def button():
    button_list = [
            KeyboardButton("Показать инлайн кнопки"),
            KeyboardButton("Показать инлайн кнопки"),
            KeyboardButton("Показать инлайн кнопки"),
        ]
    return ReplyKeyboardMarkup(build_menu(button_list, 3))


def inline_button():
    button_list = [
        InlineKeyboardButton("Узнать мнение других!", callback_data='yes'),
        InlineKeyboardButton("Узнать мнение других!", callback_data='yes'),
        InlineKeyboardButton("Узнать мнение других!", callback_data='yes'),
        InlineKeyboardButton("Узнать мнение других!", callback_data='yes'),
    ]
    return InlineKeyboardMarkup(build_menu(button_list, 3))
