import sqlite3

# crear instancia de db

db = sqlite3.connect('database.db') # si la db no existe, sqlite3 la crea con ese nombre y la conecta

# crear cursor para ejecutar código sql

cursor = db.cursor()  #instancio el cursor en una variable

cursor.execute('SELECT * FROM personas') # ejecuta el código sql y guarda el resultado en el cursor


primer_dato = cursor.fetchone() # obtiene el primer dato del cursor en formato tupla

print(primer_dato)

datos = cursor.fetchall() # obtiene todos los datos del cursor como una lista de tuplas

print(datos)