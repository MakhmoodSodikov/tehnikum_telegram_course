class User():  # Класс User
    def __init__(self, name, age):  # Функция инициализации, принимающая на вход объект, который вызывает класс User.
        self.name = name
        self.age = age

    def older(self, user2):  # Функция сравнения 2 пользователей по возрасту.
        if self.age > user2.age:
            return self.name
        else:
            return user2.name

Bob = User('Bob', 20) # Пользователь Bob
Dan = User('Dan', 35) # Пользователь Dan
print(Bob.older(Dan))

#####################################################################################################################
