fem_counter = 0  #  Счётчик женщин нашей базы данных.

database = [['Anna', 19, 'female'],
            ['Daniel', 20, 'male'],
            ['Andy', 4, 'male']]  # База данных типа list() с именем, возрастом и полом.

for stroka in database:  # Переменная (stroka) будет обновляться каждый раз на 1, пока не кончится список.
    if stroka[2] == 'female':  # Если в элементе[2] - 'female' - то обновляем счётсчик женщин.
        fem_counter += 1
print(fem_counter)