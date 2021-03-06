#  Срезка строк. Строка по факту является массивом, по этому можно выводить отдельные символы строки.
s = 'tehnikum'
print(s[2])  # Программа выведет 'h'
print(s[2:4]) # Программа выведет 'hn' - так как 'h' - это второй элемент строки (s), а 'n' - второй.
print(s[-1])  # Это эквивалентно функции print(s[len(s)-1])
print(s[0:6:2])  # Вырезка с 0 по 6 элемент с шагом в 2
print(s[-4:])  # С -4 элемента до конца
print(s[::-1])  # Считывание слова в обратном порядке с шагом 1.