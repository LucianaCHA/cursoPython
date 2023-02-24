import sqlite3

from crudfunciones import create_record, edit_record, show_record, show_all

db = sqlite3.connect('database.db')

cursor = db.cursor()

while True:
    print('''
    [1] Agregar persona (Create)
    [2] Ver dato de persona (Read)
    [3] Actualizar persona (Update)
    [4] Borrar persona (Delete)
    [5] Ver todo
    [6] Salir
    ''')
    opcion = input('Elija una opción: ')

    if opcion == '1':
        create_record(db, cursor)
    elif opcion == '2':
        show_record(cursor)
    elif opcion == '3':
        edit_record(db, cursor)
    elif opcion == '4':
        id = input('ID: ')
        cursor.execute(f"DELETE FROM personas WHERE id = {id}")
        db.commit()
    elif opcion == '5':
        show_all(cursor)

    elif opcion == '6':
        break
    else:
        print('Opción inválida')
