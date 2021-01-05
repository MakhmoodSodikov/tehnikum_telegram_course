import pickle

file = open('data.txt', 'rb')
# открываем файл с ключом 'rb' - read bites ( чтение по байтам )
users_copy = pickle.load(file)
# снимаем копию данных из файла в новый лист ( разконсервировываем) )
print(users_copy)
# выводим нашу копию в консоль
file.close()
# закрываем наш файл
file = open('data.txt', 'wb')

users_copy = pickle.load(file)

users_copy.append(input('Введите ваше имя: '))
# добавим имя, которое введёт пользователь. Оно сохранится перманентно
pickle.dump(users_copy, file)
print(users_copy)
file.close()