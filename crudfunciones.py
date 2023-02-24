""" Provides functions to handle crud in db"""


def valid_record(string):
    """Check for valid data"""
    if (
        string.isalpha() and
        string.isalpha() and
        3 <= len(string) <= 50 and
        3 <= len(string) <= 50
    ):
        return True
    else:
        return False


def create_record(db_name, cursor):
    """expects a db and its cursor, to add name and surname to db """
    first_name = input('Name: ')
    last_name = input('Lastname: ')

    if (
        valid_record(first_name) and
        valid_record(last_name)
    ):
        cursor.execute(
            "INSERT INTO People(Name, Surname) VALUES(?,?)", (first_name, last_name))

        db_name.commit()

        print('Record added successfuly!')
    else:
        print('Error! Insert valid data')


def show_record(cursor):
    """ Print a record if receives a valid id"""
    id_record = input('Insert Id: ')

    if id_record.isnumeric():
        data = cursor.execute(
            f'SELECT Name, Surname FROM People WHERE ID={id_record}')
        if data is None:
            print('Does not exist id')
        else:
            print('We found: ', cursor.fetchone())
    else:
        print('Invalid Id')


def show_all(cursor):
    """Prints a tuple with all records in db"""
    cursor.execute('SELECT * FROM People')
    people = cursor.fetchall()

    for person in people:
        print(f'{person[1]} {person[2]}')


def edit_record(db_name, cursor):
    """ Receives an id and if it valid edits db"""
    id_record = input('ID: ')

    data = cursor.execute(
        f'SELECT Name, Surname FROM People WHERE ID={id_record}')

    if data is None:
        print('Invalid id')
    else:
        data = cursor.fetchone()
        old_first_name = data[0]
        old_last_name = data[1]

        print(f'Current data: {old_first_name} {old_last_name}')

        first_name = input('Insert new name (Press enter to keep current): ')
        if first_name == '' :
            first_name = old_first_name
        else:
            if not valid_record(first_name):
                first_name = old_first_name
                print('Invalid name, cannot update')
        last_name = input('Insert new surname (Press enter to keep current): ')
        if last_name == '':
            last_name = old_last_name
        else:
            if not valid_record(last_name):
                last_name = old_last_name
                print('Invalid surname, cannot update')

        cursor.execute(
            f'UPDATE People SET Name= "{first_name}", Surname="{last_name}" WHERE id={id_record}')

        db_name.commit()

        print(f'Updated data: {first_name} {last_name}')
