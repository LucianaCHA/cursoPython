import sqlite3

# crear instancia de db

db = sqlite3.connect('database.db') # si la db no existe, sqlite3 la crea con ese nombre y la conecta

# crear cursor para ejecutar código sql

cursor = db.cursor()  #instancio el cursor en una variable

# cursor.execute(" INSERT INTO personas VALUES (NULL, 'Juan', 'Perez lINDO', 28, '10-8-1952') ") # PREPARA DATA PARA GUARDAR EN LA DB

# db.commit() # ejecuta los comandos guardados en el cursor 

# Como el id es autoincremental y en verdad no lo deberia ingresar el usario, lo dejamos en NULL pero puede mejorarse indicando los campos que se quieren ingresar y sus valores

# cursor.execute( "INSERT INTO personas(first_name, last_name, dni, birthdate) VALUES ('Ivan', 'Rodriguez', 42, '10-8-1972')")

# db.commit()

# tambien puedo cargar varios datos a la vez y registros desde variables

# registro1 = ('William', 'Gibson', 242, '10-8-1972')

# cursor.execute( "INSERT INTO personas(first_name, last_name, dni, birthdate) VALUES (?,?,?,?)", registro1)

# db.commit()

registros = [
  ('Stephen', 'King', 3542, '4-8-1952'),
  ('Jorge', 'Luis Borges', 442, '12-12-1872'),
  ('Isaac', 'Asimov', 5420, '10-5-1472'),
  ('Frank', 'Herbert', 6542, '10-8-1372'),
  ('Jules', 'Verne', 7462, '10-8-1972'),
]

cursor.executemany( "INSERT INTO personas(first_name, last_name, dni, birthdate) VALUES (?,?,?,?)", registros)

db.commit()