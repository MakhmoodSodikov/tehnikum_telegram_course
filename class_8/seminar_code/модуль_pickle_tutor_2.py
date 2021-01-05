import pickle

file = open('data.txt', 'rb')
# открываем файл с ключом 'rb' - read bites ( чтение по байтам )
users_copy = pickle.load(file)
# снимаем копию данных из файла в новый лист ( разконсервировываем) )
print(users_copy)
# выводим нашу копию в консоль
file.close()
# закрываем наш файл