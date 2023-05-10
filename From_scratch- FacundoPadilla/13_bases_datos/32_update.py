import sqlite3 

db = sqlite3.connect('database.db')
cursor = db.cursor()

cursor.execute("UPDATE personas SET first_name = 'Juan' WHERE id = 2") # actualiza el registro con id = 2, MUY IMPORTANTE: SIEMPRE USAR WHERE PARA NO ACTUALIZAR TODA LA COLUMNA

cursor.close()

db.commit()