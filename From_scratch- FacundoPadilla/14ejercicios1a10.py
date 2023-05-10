from utils import is_numeric_validation

# 1: Dado un nro natural x mostrar su ultimo digito

number = input('Insert a number: ')

def print_last_digit(x : int) -> str:
    if x.isnumeric == False:
        return 'Invalid input. Insert a number higher tan zero'
    else:
        return x[len(x)-1]

#even more pythonic

def print_last(x : int) -> str:
    check_value = is_numeric_validation(x)
    if check_value == True:
        return x[-1]
    else:
        return check_value

print(print_last(number))

# 2 Dado un nro natural contar la antidad de igitos que posee
def digit_counter(x : int) -> int:
    check_value = is_numeric_validation(x) 
    if check_value == True:
        return len(x)
    else:
        return check_value
print(digit_counter(number))

#using for is posible to count nuber of iterations

c= 0 
for digito in number:
    c += 1
print('el numero de digitos es ', c)


#3 Dado un nro natural x contar cantidad de digito pares e impares

def count_odds_and_even(x : int) -> str:
    check_value = is_numeric_validation(x)
    if check_value == True:
        count_odds = 0
        count_even = 0
        for digit in x:
            if int(digit) % 2 == 0:
                count_even +=1
            else:
                count_odds +=1
        return f'In number {x} {count_even} digits are even and {count_odds} are odds.'
    else:
        return check_value

print(count_odds_and_even(number))

#4 Dado un nro natural x , sumar todos sus digitos. mostrar suma obtenida

def sum_all(x : int ) -> str:
    check_value = is_numeric_validation(x)
    if check_value == True:
        sum :int = 0
        for digit in x:
            sum += int(digit)
        return f'Total is {sum}.'
    else:
        return check_value

print(sum_all(number))
#list and methods

lista =[]
for digito in number:
    lista.append(int(digito))
print ('Total, using list methods is: ', sum(lista))

#5 Dado un nro natural determinar si es capicua
def is_capicua(n : int) -> bool:
    check_value = is_numeric_validation(n)

    if check_value == True:
        i : int = len(n)-1
        reverse :str = ''
        for i in range(i, -1, -1):
            reverse += n[i]
        if reverse == n:
            return True
        else:
            return False
    else:
        return check_value

print(is_capicua(number))

#solucion super cheta que ni se me pasó porla mente

def check_capicua(n : int )-> str:
    check_value = is_numeric_validation(n)

    if check_value == True:
        if n == n[::-1]:
            return 'Is capicúa'
        else:
            return "Isn't capicua"
    else:
        return check_value
print(check_capicua(number))

#6 dado un numero entero x mostrar sus N primeras potencias

base = int(input('Insert a number: '))
power = int(input('Choose powers to check: '))

def power_list(x : int, N : int) -> int:
    powers = []
    while (N > 0):
        powers.append(f'{x } elevado a {N} es {pow(x,N)}')
        N -= 1
    return powers
    
print(power_list(base, power))


# base = input('Insert a number: ')
# power = input('Choose powers to check: ')

def power_list(x : int, N : int) -> int:
    try:
        x = int(input("Insert a number: "))
        N = int(input('Choose powers to check: '))
    except ValueError:
        print("iNSERT A NUMBER")
    else:
        if N > 0 :
            powers = []
            while (N > 0):
                powers.append(f'{x } elevado a {N} es {pow(x,N)}')
                N -= 1
            return powers
        else:
            return 'Invalid input'
   
    
print(power_list())

#7 Dado un nro natural xmostrar tods sus divisores

def divisores_list (x : int) -> list:
    check_natural_number = is_numeric_validation(x)
    if check_natural_number == True:
        divisors = []
        aux = 1
        number = int(x)
        # while (number > aux):
        #     aux += 1
        #     if number % aux == 0:
        #         divisors.append(aux)
        for aux in range(1, number):
            if number % aux == 0:
                divisors.append(aux)

        return divisors
    else:
        return check_natural_number
print(divisores_list(number))

#9 dado u nro natural x, contar todos sus divisores

def divisores_list (x : int) -> list:
    check_natural_number = is_numeric_validation(x)
    if check_natural_number == True:
        divisors = []
        aux = 1
        number = int(x)
        # while (number > aux):
        #     aux += 1
        #     if number % aux == 0:
        #         divisors.append(aux)
        for aux in range(1, number):
            if number % aux == 0:
                divisors.append(aux)

        return divisors
    else:
        return check_natural_number
print(divisores_list(number))

def count_divisors(x : int):
    return f'The number {x} has {len(divisores_list(x))} divisors'
print(count_divisors(number))

def sum_divisors(x : int):
    check_natural_number = is_numeric_validation(x)
    if check_natural_number == True:
        counter = 0
        divs = 1 
        number = int(x)
       
        for divs in range(1, number):
            if number % divs == 0:
                counter += divs

        return f'Result: {counter}'
    else:
        return check_natural_number
print(sum_divisors(number))

#10 Dados dos numeros nauales A y B mostrar sus divisores comunes

number1 = input('Insert a number : ')
number2 = input('Insert another : ')
def divisors_in_common(A : int, B : int) -> list:
    numberA = int(A)
    numberB = int(B)
    check_natural_number = is_numeric_validation(A) and is_numeric_validation(B)
    if check_natural_number == True:
        divisors = []
        divs = 1
        for divs in range(1, numberA):
            if numberA % divs == 0 and numberB % divs ==0:
                divisors.append(divs)      
        
        return divisors
        

    else:
        return check_natural_number

print(divisors_in_common(number1, number2))