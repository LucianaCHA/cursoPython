from statistics import mean
from utils import is_numeric_validation, is_integer_validation, create_user_list

# ejercicio 21 
"""
A una fiesta asistieron personas de diferentes edades y sexos. Construir un algoritmo que dadas edades y géneros calcule
Cantidad de hombres y mujeres
Promedio de edades por géneros
Edad de las persona más joven qye asistió
"""
#returns a list of attendants asking user for number of attendants, and then creaes it with age, name and genre

def create_attendants_list():
    attendants = []
    attendant_data ={}
    n = input('Insert number of attendants: ')
    check_valid_n = is_numeric_validation(n)
    if check_valid_n:
        for i in range(int(n)):
            id = i+1
            name = input(f"Insert attendant's number {id} name: ")
            age = input(f"Insert attendant's number {id} age: ")
            gender = input("Male or Female?, insert M or F: ")

            check_valid_age = is_numeric_validation(age)
            check_valid_gender = 'M' or 'F'
            if check_valid_age:
                if check_valid_gender:
                    attendant_data = {
                        'id': id,
                        'name': name,
                        'age': int(age),
                        'gender': gender
                    }
                    attendants.append(attendant_data)
                else:
                    return 'Insert F for female and M for Male'
            else:
                return 'Insert a valid age'
        return attendants

#for variables received as arguments, if they are 0, they are replaced by 1 to avoid division by zero, if not, they are returned with no chenga

def avoid_division_by_zero(*args):
    new_args = []
    for arg in args:
        if arg == 0:
            new_args.append(1)
        else:
            new_args.append(arg)
    return new_args

def attendants_list():
    attendants = create_attendants_list()

    males : int = 0
    females : int = 0
    females_age_sum : int = 0
    males_age_sum : int = 0

    youngest_attendant= attendants[0]['age']

    for attendant in attendants:
        if attendant['gender'] == 'M':
            males +=1
            males_age_sum += attendant['age']
        else:
            females +=1
            females_age_sum += attendant['age']
        if attendant['age'] < youngest_attendant:
            youngest_attendant = attendant['age']
            
    check = avoid_division_by_zero(males, females)
    
    return f'Men = {males}, average age = {males_age_sum/check[0]}; Women = {females}, average age = {females_age_sum/check[1]}; youngest attendant age = {youngest_attendant} '

# print(attendants_list())

#22 Determinar si un numero X es perfecto, es decir, es igual a la suma de sus divisores propios

def perfect_number():
    number = input('Insert a number: ')
    check_number = is_numeric_validation(number)
    if check_number:
        divisors = []
        for i in range(1, int(number)):
            if int(number) % i == 0:
                divisors.append(i)
        if sum(divisors) == int(number):
            return f'{number} is a perfect number'
        else:
            return f'{number} is not a perfect number'
    else:
        return 'Insert a valid number'

# print(perfect_number())

#23 calcular cuantos segundos tiene una hora dada

def seconds_in_time():
    hour = input('Insert a hour: ')
    check_format = hour.split(':')
    invalid_format = False

    print(check_format)
    for item in check_format:
        check_number = is_numeric_validation(item)
        if check_number != True:
            invalid_format = True
            return check_number

    if len(check_format) == 3 and invalid_format == False:
        seconds = int(check_format[0]) * 3600 + int(check_format[1]) * 60 + int(check_format[2])
        return seconds
    else:
        return 'Insert a valid hour (hh:mm:ss)' 
       

# print(seconds_in_time())

#24 Print the first x prime numbers

def print_primes():
    number : int = input('Insert a number: ')
    check_valid_number = is_numeric_validation(number)
    primes : list = []

    if check_valid_number:
        check_is_prime : int = int(number)
        aux :int = 2
        while (aux < is_prime):
            if is_prime % aux == 0:
                return False
            else:
                aux += 1



                
