f = open('text.txt', 'w')  # 'w' - вписывание новых данных в файл text.txt

f.write('line1')
f.write('\nline2')  # Знак '\n' отвечает за Enter перед строкой.
f.write('\nline3')
f.close()  # Пока файл не закроется, изменения не появятся в файле.

########################################################################

f = open('text.txt', 'w')
for i in range(0,1000):
    f.write('line' + str(i) + '\n')
f.close()