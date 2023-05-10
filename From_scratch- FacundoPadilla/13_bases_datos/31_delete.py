import sqlite3

# crear instancia de db
db = sqlite3.connect('database.db')

cursor = db.cursor()
cursor.execute("DELETE FROM personas WHERE id = 1") # borra el registro con id = 1, MUY IMPORTANTE: SIEMPRE USAR WHERE PARA NO BORRAR TODA LA TABLA

cursor.close()

db.commit()