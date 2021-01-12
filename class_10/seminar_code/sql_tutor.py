import sqlite3
# Подключаем модуль базы данных SQL

conn = sqlite3.connect('database.sqlite')
# Коннектим базу данных 'database.sqlite' к модулю SQL.

cursor = conn.cursor()
# Указываем на конкретную базу данных, которую мы создали и подключили к модулю SQL.

# SQL запрос 'execute' обрабатывает запрос, который получает.
cursor.execute(''' 
create table if not exists General_Table ( Имя text,
                                        Возраст integer, 
                                        Пол text, 
                                        Город text,
                                        Номер телефона text) 
''') # Создаём таблицу с разными столбцами.
cursor.execute('''
insert into General_Table values ('Роман', '19', 'М', 'Ташкент', '+998970042478')
''') # Добавляем данные в нашу таблицу.
conn.commit()
# Подтверждаем добавление.
print(cursor.execute('''
select Имя
from General_Table
where Город='Ташкент'
''').fetchall())

cursor.execute('''
delete from General_Table
where Возраст > 20
''') # Удаляем из базы данных всех, чей возраст больше 20