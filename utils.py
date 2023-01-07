#usefull functions for the project

#function to validate if the input is a number
import re


def is_numeric_validation(value):
    if value.isnumeric() == False:
        return 'Invalid input. Insert a number higher tan zero'
    else:
        return True
#function to validate if the input is an integer
def is_integer_validation(user_input):
    try:
        int(user_input)
        it_is = True
    except ValueError:
        it_is = False
    return it_is
#function to create a list of N elements

def create_user_list():
    user_list: list = []
    n = input('Insert N: ')
    check_valid_n = is_numeric_validation(n)
    if check_valid_n:
        for i in range(int(n)):
            x = input('Insert a number: ')
            check_valid_x = is_integer_validation(x)
            if check_valid_x:
                user_list.append(int(x))
            else:
                return 'Insert a valid number'
        return user_list
    else: 
        return check_valid_n

def is_prime_number(number):
    check_valid_int = is_integer_validation(number) and number > 0
    
    if  check_valid_int:
        if number == 1:
            return False
        elif number == 2:
            return True
        else:
            for i in range(2, number):
                if number % i == 0:
                    return False
            return True
    else:
        return check_valid_int

def create_matrix():
    matrix = []
    n = input('Insert N: ')
    m = input('Insert M: ')

    valid_n = is_numeric_validation(n)
    valid_m= is_numeric_validation(m)
    if valid_n and valid_m:
        for j in range(int(n)):
            row : list = []
            matrix.append(row)
            for i in range(int(m)):
                x  = input(f'Insert number for row {i+1}, column {j+1}: ')
                valid_x = is_numeric_validation(x)
                if valid_x:
                    row.append(int(x))
                else:
                    return is_numeric_validation(x)
        return matrix
    else:
        return is_integer_validation(n)

def create_matrix_alphanumerics_digit():
    matrix = []
    n = input('Insert N: ')
    m = input('Insert M: ')

    valid_n = is_numeric_validation(n)
    valid_m= is_numeric_validation(m)
    if valid_n and valid_m:
        for j in range(int(n)):
            row : list = []
            matrix.append(row)
            for i in range(int(m)):
                x  = input(f'Insert number or character {i+1}, column {j+1}: ')
                #check valid char ornumber with regex
                valid_x = re.compile(r'^[a-zA-Z0-9]+$')
                if valid_x:
                    row.append(x)
                else:
                    return 'Insert a valid character or number' 
        return matrix
    else:
        return is_integer_validation(n)

def create_matrix_base(base):
    matrix = []
    n = input('Insert N: ')
    m = input('Insert M: ')

    valid_n = is_numeric_validation(n)
    valid_m= is_numeric_validation(m)
    if valid_n and valid_m:
        for j in range(int(n)):
            row : list = []
            matrix.append(row)
            for i in range(int(m)):
                x  = input(f'Insert number for row {i+1}, column {j+1}: ')
                valid_x = 0 <= int(x) < base
                if valid_x:
                    row.append(int(x))
                else:
                    return 'Insert a valid number (for base {base} should be between 0 and {base})'
        return matrix
    else:
        return is_integer_validation(n)
        
