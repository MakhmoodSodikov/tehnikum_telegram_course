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
            KeyboardButton("Показать инлайн-кнопки"),
            KeyboardButton("кнопка1"),
            KeyboardButton("кнопка2"),
            KeyboardButton("кнопка3"),
    ]

    return ReplyKeyboardMarkup([[button_list[0], button_list[1], button_list[3]],
                                [button_list[2], ]])


def generate_buttons(item_name, n=6):
    buttons_list = []

    for i in range(1, n+1):
        button_caption = str(i)
        callback_data = item_name + '_' + button_caption
        buttons_list.append(InlineKeyboardButton(button_caption, callback_data))

    return InlineKeyboardMarkup(build_menu(buttons_list, n // 2))


def inline_button():
    button_list = [
        InlineKeyboardButton("Нажми меня", callback_data='test1234_1'),
        InlineKeyboardButton("Нажми меня", callback_data='yes'),
        InlineKeyboardButton("Нажми меня", callback_data='yes'),
        InlineKeyboardButton("Нажми меня", callback_data='yes'),
    ]

    return InlineKeyboardMarkup(build_menu(button_list, 3))


def get_phone():
    button_list = [KeyboardButton("Отправить контакты", request_contact=True)]
    return ReplyKeyboardMarkup([button_list], resize_keyboard=True)


def start_order():
    button_list = [KeyboardButton("Начать заказ"),
                   KeyboardButton("История покупок")]
    return ReplyKeyboardMarkup([button_list], resize_keyboard=True)


def get_location():
    button_list = [KeyboardButton("Отправить локейшн", request_location=True)]
    return ReplyKeyboardMarkup([button_list], resize_keyboard=True)
