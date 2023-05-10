""" Provides functions to handle crud in db"""
import sqlite3

def connect_db():
    """ Open db connection"""
    try:
        database = sqlite3.connect('database.db')
        return database, database.cursor()
    except Exception:# no es unabuena practica
        print("Can 't connect database'")
        return 0



def valid_record(string):
    """Checks if string is long enough to be a record in db"""
    return (
        string.isalpha() and
        string.isalpha() and
        3 <= len(string) <= 50 and
        3 <= len(string) <= 50
    )

def valid_id(cursor):
    """REceives an id an look for it in db, if existe return data else error message"""
    id_record = input('Insert Id: ')

    if id_record.isnumeric():
        cursor.execute(
            f'SELECT Name, Surname FROM People WHERE ID={id_record}')

        result = cursor.fetchone()
        if result is None:
            return {
                'result': 'Id does not exists',
                'id': id_record}
        return {
            'result': result,
            'id': id_record
        }

    return {
        'result' : 'Invalid Id',
        'id': id_record
        }

def valid_input(old_name, kind):
    """receives two string"""
    name = input(f'Insert new {kind} (Press enter to keep current): ')
    if name == '':
        name = old_name
    else:
        if not valid_record(name):
            name = old_name
            print('Invalid name, cannot update ',{kind})
    return name

def create_record():
    """expects a db and its cursor, to add name and surname to db """
    db_name, cursor = connect_db()

    first_name = input('Name: ')
    last_name = input('Lastname: ')

    if (
        valid_record(first_name) and
        valid_record(last_name)
    ):
        cursor.execute(
            "INSERT INTO People(Name, Surname) VALUES(?,?)", (first_name, last_name))
        cursor.close()
        db_name.commit()

        print('Record added successfuly!')
    else:
        print('Error! Insert valid data')
    db_name.close()

def show_record():
    """ Print a record if receives a valid id"""
    db_name, cursor = connect_db()

    response = valid_id(cursor)
    data = response['result']
    if isinstance(data, str):
        print(data)
    else:
        print(f'We found : {data[0]} {data[1]}')
    db_name.close()

def show_all():
    """Prints a tuple with all records in db"""
    db_name, cursor = connect_db()
    cursor.execute('SELECT * FROM People')
    people = cursor.fetchall()
    cursor.close()

    for person in people:
        print(f'{person[1]} {person[2]}')
    db_name.close()

def edit_record():
    """ Receives an id and if it is valid edits db"""
    db_name, cursor = connect_db()
    response = valid_id(cursor)

    data = response['result']
    id_record = response['id']

    if isinstance(data, str):
        return data

    old_first_name = data[0]
    old_last_name = data[1]

    print(f'Current data is: {old_first_name} {old_last_name}')

    first_name = valid_input(old_first_name, 'first name')
    last_name = valid_input(old_last_name, 'last name')

    cursor.execute(
        f'UPDATE People SET Name= "{first_name}", Surname="{last_name}" WHERE id={id_record}')
    cursor.close()

    db_name.commit()

    print(f'Updated data: {first_name} {last_name}')
    return 'Record updated successfuly!'

def delete_record():
    """ Receives an id and if it is valid deletes record from db"""
    db_name, cursor = connect_db()
    response = valid_id(cursor)

    data = response['result']
    id_record = response['id']

    if isinstance(data, str):
        return data

    cursor.execute(f'DELETE FROM People WHERE id={id_record}')
    cursor.close()

    db_name.commit()

    print(f'Record {id_record} deleted successfuly!')
    return 'Record deleted successfuly!'
