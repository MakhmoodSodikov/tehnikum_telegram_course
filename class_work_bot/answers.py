import messege as msg

eng_answers = {'Hello': msg.en_hello,
               'Bye': msg.en_bye,}

rus_answers = {'привет': msg.ru_hello,
               'пока': msg.ru_bye,
               'Сколько тебе лет?': msg.ru_age}

global_answers = {'rus': rus_answers,
                  'eng': eng_answers}
