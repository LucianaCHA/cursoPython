""" Crud pyton + sql3 """
from crudfunciones import create_record, delete_record, edit_record, show_all, show_record

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
        create_record()
    elif option == '2':
        show_record()
    elif option == '3':
        edit_record()
    elif option == '4':
        delete_record()
    elif option == '5':
        show_all()
    elif option == '6':
        print('Connection closed')
        break
    else:
        print('Invalid option!')
