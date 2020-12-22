database = {'Name' : ['Roman', 'Anna'],
     'Age' : [18, 23],
     'Gender' : ['male', 'female']}

names = database['Name']  # "Сохраним" наш список имён в новый список (names).
ages = database['Age']  # "Сохраним" наш список возрастов в новый список (ages).
genders = database['Gender']  # "Сохраним" наш список полов в новый список (genders).
new_name = input()  # Вводим новое имя.
new_age = input()  # Вводим новый возраст.
new_gender = input()  # Вводим новый гендер(пол).
names.append(new_name)  # Добавляем в старый список имён новое имя.
ages.append(new_age)  # Добавляем в старый список возрастов новый возраст.
genders.append(new_gender)  # Добавляем в старый список гендеров новый гендер.
database['Name'] = names  # Приравниваем обновлённый лист с именами к ключу 'Name' в словаре (database)
database['Age'] = ages  # Приравниваем обновлённый лист с возрастами к ключю 'Age' в словаре (database)
database['Gender'] = genders  # Приравниваем обновлённый лист с гедерами к ключю 'Gender' в словаре (database)
print(database)  # Выводим весь словарь с обновлённым ключом 'Name'