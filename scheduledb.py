import sqlite3

connection = sqlite3.connect("schedule.db")
cursor = connection.cursor()

''' TABELA USUARIOS '''

cursor.execute("CREATE TABLE agenda_usuarios (name TEXT NOT NULL, email TEXT NOT NULL UNIQUE, password TEXT NOT NULL)")

cursor.execute("INSERT INTO agenda_usuarios values ('Tiago Farias Barbosa', 'tfb.snf21@uea.edu.br', '123456')")

''' TABELA EVENTOS '''

'''

cursor.execute("DROP TABLE agenda_eventos")

cursor.execute("CREATE TABLE agenda_eventos (titulo TEXT NOT NULL, descricao TEXT NOT NULL, data TEXT NOT NULL, id_usuario INTEGER NOT NULL, FOREIGN KEY(id_usuario) REFERENCES agenda_usuarios(rowid))")

'''

connection.close()
