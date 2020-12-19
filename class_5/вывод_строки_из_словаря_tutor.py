database = {'Name' : ['Roman', 'Anna'],
     'Age' : [18, 23],
     'Gender' : ['male', 'female']}

for key in database.keys():  # Пока key находится в ключах нашего цикла ('Name', 'Age', 'Gender' ) и с проходом каждого цикла key будет равен каждому ключу.
    vals = database[key]  # Приравниваем переменную vals к (key) от словаря (database).
    print(vals[0])  # Выводит 0 элемент от ключа, к которому приравнен переменную vals.