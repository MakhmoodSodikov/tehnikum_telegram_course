from database import data  # Мы вызываем переменную data из модуля database, в которой у нас хранится переменная
import database  # Если мы импортируем модуль так, то к переменным нам нужно обращаться так: database.переменная
# Тоесть в случае с циклом ниже мы бы написали условие как:
# for i in database.data.keys(): и т.д. обращаясь к переменным через database.переменная
# Это можно облегчить, если приравнять другую переменную к длинному названию:
# our_data = database.data и дальше использовать our_base
for i in data.keys():
    vals = data[i]
    print(vals[0])
    
##########################################################################

# Для вызова модулей из папок использовать '.'
# Тоесть, если наш модуль в папке 'box', то мы вызовем модуль оттуда командой from box.название модуля imbort название переменных

import random as r  # для обращения к модулю рандом используя не random, а r
print(r.randrange(0, 100, 2))  # Вывод рандомного числа от 0 до 100 с шагом 2 ( чётные числа )