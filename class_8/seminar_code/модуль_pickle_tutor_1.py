import pickle
# модуль pickle используется для "косервации" каких либо данных
users = ['Roman', 'Anna', 'Makhmood', 'Daniel']
# создаём лист users с именами пользователей
file = open('data.txt', 'wb')
# открываем файл с ключом 'wb' - write bites ( запись по байтам )
pickle.dump(users, file)
# передаём лист users в file
file.close()
# закрываем наш файл