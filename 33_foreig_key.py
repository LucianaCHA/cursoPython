import sqlite3

db = sqlite3.connect('database.db')
cursor = db.cursor()

cursor.execute("SELECT * FROM hijo")

hijos = cursor.fetchall()

print(hijos)

cursor.close()