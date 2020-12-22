def a_greater():  # Создание функции с именем a_greater
    print(a , 'greater')  # Код внутри функции. Он такой же как и код. В нём могут быть любые конструкции
def a_less():
    print(a , 'less')

a = int(input())

if a < 0:
    a_less()  # Вызов функции a_less. При вызове функции запускается код, находящийся в функции
else:
    a_greater()