import sqlite3

from crudfunciones import create_record, delete_record, edit_record, show_all, show_record



db = sqlite3.connect('database.db')

cursor = db.cursor()

while True:
    print('''
    [1] New record (Create)
    [2] See record data (Read)
    [3] Update record (Update)
    [4] Delete record (Delete)
    [5] Show all records
    [6] Exit
    ''')
    option = input('Choose an option: ')

    if option == '1':
        create_record(db, cursor)
    elif option == '2':
        show_record(cursor)
    elif option == '3':
        edit_record(db, cursor)
    elif option == '4':
        delete_record(db, cursor)
    elif option == '5':
        show_all(cursor)
    elif option == '6':
        break
    else:
        print('Invalid option!')
