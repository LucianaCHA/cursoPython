# #ejercicio 1 'hol mundo'

# def holamundo():
#     print('hola mundo')
#     return holamundo
# holamundo()

# #ejercicio 2 script que almacena Hoa mundo en una variable y luego la imprime

# def holamundo():
#     s : str= 'Hola mundo'
#     print(s)

# holamundo()

# #ejercicio 3 script to ask userś name and greet them

# name : str = input('Tell me your name: ')

# def greet(name: str) -> str:
#     return f'Hello  {name.capitalize()}!'

# print(greet(name))

#4 write a script that ask userś name and a number and print that name that number of times

# name : str = input('Tell me your name: ')
# number : int = int(input('Tell me a number: '))
# def greet(name: str, number: int) -> str:
#     return f'Hello  {name.capitalize()}!\n' * number

# print(greet(name, number))

##5 write a script that ask for users name and prints the name and the length of the name

# name: str = input('Tell me your name:')

# def greeting(name : str) -> str:
#     return f'{name.upper()} has {len(name)} characters'
# print(greeting(name))

##6 write a script that asks user for labour hours and cost per hour and prints the total cost

# hours : int = int(input('Tell me the hours you worked: '))
# cost : int = int(input('Tell me the cost per hour: '))

# def total_cost(hours :int, cost: int) -> int:
#     return hours * cost

# print(f'The total cost is {total_cost(hours, cost)}')

# #7 write a script that asks the price of aproduct and returns IVa (21%) and original cost

# price :int = int(input('Ingress final price: '))

# def calcualte_original_cost(price:int) ->int:
#   iva :int = price * 0.21
#   cost :int = price-iva
#   print(f'Original price : {cost}, IVA: {iva}.')

# calcualte_original_cost(price)

# #8 given two numbers print the lower one

# number1 : int = int(input('Insert number 1: '))
# number2 : int = int(input('Insert number 2: '))

# def show_minor(num1: int, num2: int) -> int:
#     if num1 < num2:
#         print(f'Between {num1} and {num2} the lower value is {num1} ')
#     elif num1 == num2:
#         print(f'The numbers are equals ')
#     else:
#         print(f'Between {num1} and {num2} the lower value is {num2} ')

# show_minor(number1, number2)

# #9 asks for userś age and say if is or not major

# age : int = int(input('Tell me your age: '))

# def is_major(age : int )-> int:
#     if age >= 18:
#         print('You are major age')
#     else:
#         print('You are not major')

# is_major(age)

# #10 ask user for a word and repeat it 10 times

# word: str = input('Type a word: ')

# def repeat_ten_times(s: str) -> str:
#     n=0
#     while (n < 10):
#         print(s)
#         n+= 1

# repeat_ten_times(word)

# def repeat_ten_times_for_version(s: str) -> str:
#     for word in range(10):
#         print(s)

# repeat_ten_times_for_version(word)

#11 ask user for a number and prin if is odd or not

# number : int = int(input('Insert a number: '))

# def odd_or_even(n: int) -> str:
#     if n%2 == 0:
#         print(f'{n} is even.')
#     else:
#         print(f'{n} is odd.')
# odd_or_even(number)

#12 write a scrit that ask for  a pósitive integer and then print to screen from 1 to thatnumber all odd nuymbers i range

# def write_all_odds(n : int) -> int:
#     if n < 0 :
#         print('Insert a positive number')
#     elif n == 1:
#         print('1')
#     else:
#         i = 1
#         # answer = '1'
#         # while (i < n):
#         #     i += 2
#         #     answer = answer + ',' + str(i)
#         # print(answer)
#         # for cycle version
#         for i in range(1, n+1):
#             if i%2 != 0:              
#                 print(i, end=', ')
# write_all_odds(number)

#13 write a scrpti that given a number prints the regresive count separated wqith commas

# def regresive_count(n:int) -> int:
#     i = 0
#     answer = str(n)
#     while (i < n):
#         i += 1
#         answer = answer + ',' + str(n-i)
#     print(answer)

# regresive_count(number)

# #14 write a script that ask for a number and prints a rectangle triangle with *

# number : int = int(input('Insert a number: '))

# def build_triangle(n : int) -> str:
#   i : int = 0
#   while (i < n):
#     i += 1
#     print('*'* i)
# build_triangle(number)

# #15 Show tabla del 1 al 10 

# def tabla () -> str:
#   i = 0 
#   while (i < 10) :
#     i += 1
#     print(f'1 x {i} = {i}')

#   for i in range(1,11):
#     print(f'1 x {i} = {i}')
# tabla()

# #16 Ask user for a word and print characters one to one in reverse

# word : str = input('Insert any word: ')

# def print_reverse(string : str) -> str:
#     i : int = len(string)
#     while (i > 0):
#       i -=1
#       print(string[i])

# print_reverse(word)

# def print_reverse_for(string : str) -> str:
#     for i in range(i, -1, -1): #empiezo en i osea el final, hasta -1 porque no es inclusivo y resto de a uno
#         print(string[i])

# print_reverse(word)

#17 Write a script that asks user for a prhase an a letter, and print how many times the letter is in the prhaase
phrase : str = input('Insert a phrase: ')
character : str = input('Insert a character: ')
def repetead(string : str, char : str ) -> str :
    count = 0
    for letra in string:
        if letra == char:
            count += 1
    print(f'The character {character} is repeated {count} times')
repetead(phrase, character)