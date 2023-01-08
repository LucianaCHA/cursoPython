import re
from statistics import mean
from utils import create_matrix, create_matrix_alphanumerics_digit, create_matrix_base, is_numeric_validation, is_integer_validation, create_user_list, is_prime_number

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
        for i in range(2, int(number)+1):#+1 porque es excluyente 
            if is_prime_number(i) == True:
                primes.append(i)
        return primes
    else:
        return 'Insert a positive number'

# print(print_primes())

#25 Generar los primeros k numeros de la serie de fibonacci. Los primeros son el 0 yt el 1. el resto se calcula como la suma de los dos numeros que lo preceden. Además, indicar cuantos números primos existen en la serie generada

def fibonacci():
    number = input('Insert number for fibonacci serie: ')
    check_valid_num = is_integer_validation(number)

    number1 : int = 0
    number2 : int = 1
    serie : list = []
    primes : int = 0
    if check_valid_num:
        for i in range(int(number)):
            serie.append(number1)
            number1, number2 = number2, number1 + number2
            if is_prime_number(i) == True:
                primes += 1   
        return f'Fibonacci serie = {serie}, primes = {(primes)}'

# print(fibonacci())

# 26 dada una lista de palabras contar cuantas vocales y consonantes tiene cada palabra
def insert_word() -> str:
    word : str = input("Insert a word ('stop' to stop): ")

    if len(word) >= 3 :
        return word
    else:
        return 'Insert at least 3 characters'

def create_words_list() -> list:
    word : str = insert_word()
    if word == 'stop':
        return []
    else:
        return [word] + create_words_list()

def count_vowels_and_consonants():
    words_list : list = create_words_list()
    answer : list = []
    #reg ex eliminar caracteres especiales y espacios



    for word in words_list:
        vowels : int = 0
        consonants : int = 0
        numbers : int = 0
        #re es una libreria para trabajar con expresiones regulares, en este caso, elimina los caracteres especiales y especiales. EStrictamente hablando en realidad los reemplaza por na da ''

        for letter in re.sub(r'[^a-zA-Z0-9]', '', word):
            if letter in 'aeiouAEIOU':
                vowels += 1
            elif letter in '0123456789':
                numbers += 1
            elif letter:
                consonants += 1
        answer.append(f'Word: {word}, vowels = {vowels}, consonants = {consonants} digits = {numbers}')    
    return answer 
    

# print(count_vowels_and_consonants())

# 27 dado un texto contar cuantas vocales y consonantes tiene cada palabra

def count_vowels_and_consonants_in_text():
    text : str = input('Insert a text: ')
    words : list = text.split(' ')
    answer : list = []

    for word in words:
        vowels : int = 0
        consonants : int = 0
        numbers : int = 0

        for letter in re.sub(r'[^a-zA-Z0-9]', '', word):
            if letter in 'aeiouAEIOU':
                vowels += 1
            elif letter in '0123456789':
                numbers += 1
            elif letter:
                consonants += 1
        answer.append(f'Word: {word}, vowels = {vowels}, consonants = {consonants} digits = {numbers}')    
    return answer

# print(count_vowels_and_consonants_in_text())

#Ejercicio 27: Dada una matriz de NxM elementos , calcular el promedio de cada fila y columna, mostrar en patalla lamatriz cargada y los promedios correspondientes
def matrix_average():

    matrix = create_matrix()
    n : int = len(matrix)
    m : int = len(matrix[0])
    matrix.append([])

    for j in range(n):
        row_average = mean(matrix[j])
        matrix[j].append(f'Row average: {row_average} ')

    for i in range(m):
        column_average = mean([matrix[j][i] for j in range(n)])
        matrix[n].append(column_average)
    matrix[n].append('<= Columns average ')

    for i in matrix:
        print(i)

# (matrix_average())

#ejercicio 28, dada una matriz de caracetres , ordenar cada columna alfabeticamente

def matrix_sort():
    matrix = create_matrix_alphanumerics_digit()
    n : int = len(matrix)
    m : int = len(matrix[0])

    for i in range(m):
        column = [matrix[j][i] for j in range(n)]
        column.sort()
        for j in range(n):
            matrix[j][i] = column[j]
    for i in matrix:
        print(i)
# matrix_sort()

# ejercicio 29 dada una matriz de N x M elementos, compuest de 0 y 1 , recorrer cada una de las filas y mostrar el valor decimal equivalente

def turn_decimal():
    matrix : list = create_matrix_base(2)
    n : int = len(matrix)
    m : int = len(matrix[0])

    if type(matrix) == str:
        return matrix
    
    decimal_matrix = []
    for i in range(n):
        count = 0
        power =  (m - 1)
        for j in range(m):
            n = matrix[i][j]
            count += pow(2,power)*n
            power -=1
        decimal_matrix.append([count])
    
        print(*matrix[i], 'to decimal ', *decimal_matrix[i])

# turn_decimal()



