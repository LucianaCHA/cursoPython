#usefull functions for the project

#function to validate if the input is a number
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
    if check_valid_n == True:
        for i in range(int(n)):
            x = input('Insert a number: ')
            check_valid_x = is_integer_validation(x)
            if check_valid_x == True:
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
    