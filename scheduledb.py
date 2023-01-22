import sqlite3

connection = sqlite3.connect("schedule.db")
cursor = connection.cursor()
'''
#TABELA USUARIOS 

cursor.execute("CREATE TABLE agenda_usuarios (name TEXT NOT NULL, email TEXT NOT NULL UNIQUE, password TEXT NOT NULL)")

cursor.execute("INSERT INTO agenda_usuarios values ('Tiago Farias Barbosa', 'tfb.snf21@uea.edu.br', '123456')")
'''
''' TABELA EVENTOS '''
'''
cursor.execute("DROP TABLE IF EXISTS agenda_eventos;")

cursor.execute("CREATE TABLE agenda_eventos (titulo TEXT NOT NULL, descricao TEXT NOT NULL, data TEXT NOT NULL);")
'''
cursor.execute("SELECT * FROM agenda_eventos;")
result = cursor.fetchall()
print(result)

connection.close()
