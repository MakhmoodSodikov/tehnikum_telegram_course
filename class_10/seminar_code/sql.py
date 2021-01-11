import sqlite3

conn = sqlite3.connect('adminfile/database.sqlite')

cursor = conn.cursor()

cursor.execute(''' 
create table if not exists General_Table (ID integer, Имя text) 
''')
cursor.execute('''
insert into General_Table values ('1', 'Роман')
''')
conn.commit()