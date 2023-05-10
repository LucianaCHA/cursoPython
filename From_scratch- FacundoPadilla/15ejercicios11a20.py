from utils import is_numeric_validation, is_integer_validation, create_user_list

#11 dada una lista de N numeros naturales x, mostrar el mayor de ellos

def the_higher() -> int:
    user_list : list = []
    n = input('Insert N:')
    check_n = is_numeric_validation(n)

    if check_n == True:
        for i in range(int(n)):
            x = input('Insert a number: ')
            check_x = is_numeric_validation(x)
            if check_x == True:
                user_list.append(x)
            else:
                return check_x
        
        sorted_list : list = sorted(user_list)
        return sorted_list[len(user_list)-1]
    else:
        return check_n
        
print(the_higher())

# #12 dada una lista de N numeros naurales, mostar el menor

# def the_minor() -> int:
#     user_list : list = []
#     n = input('Insert N: ')
#     check_n = is_numeric_validation(n)

#     if check_n == True:
#         for i in range(int(n)):
#             x = input('Insert a number: ')
#             check_x = is_numeric_validation(x)
#             if check_x == True:
#                 user_list.append(x)
#             else:
#                 return check_x
        
#         return min(user_list)
#     else:
#         return check_n
        
# print(the_minor())

# #13 dada una lista de N numeros enteros ,. calcular su promedio

# def average() -> int:
#     user_list : list = []
#     sum = 0
#     n = input('Insert N: ')
#     check_n = is_numeric_validation(n)

#     if check_n == True:
#         for i in range(int(n)):
#             x = input('Insert a number: ')
#             check_x = is_integer_validation(x)
#             if check_x == True:
#                 user_list.append(x)
#                 sum += int(x)
#             else:
#                 return 'Insert an integer number'
#         return f'The average is {sum/len(user_list)} '
#     else:
#         return check_n
        
# print(average())

#usanndo package

# from statistics import mean

# def average() -> int:
#     user_list : list = create_user_list()
    
#     return f'Average is : {mean(user_list)}'

# print(average())

# #14 dada una lista ordena de N numeros, indicar si hay elementos repetidos

# def check_repeated_elements():
#     user_list : list = create_user_list()
#     # for i in user_list:
#     #     if(user_list.count(i) > 1):
#     #         print(i)
#     repeated = set([num for num in user_list if user_list.count(num) > 1])
    
#     return f'Repeated elements: {list(repeated)}.'
# print(check_repeated_elements())

# #15 Dadas dos listas , A y B, inidcar si el mayor de la lista A se encuentra en la lista B

# def check_if_higher_in_list():
#     user_listA : list = create_user_list()
#     user_listB : list = create_user_list()
#     higher = max(user_listA)
#     if higher in user_listB:
#         return f'{higher} is in {user_listB}'
#     else:
#         return f'{higher} is not in {user_listB}'

# print(check_if_higher_in_list())

# #16 dada una lista de N numeros indicar si l mismo esta ordenado de menor a mayor


def check_if_ordered():

    user_list : list = create_user_list()

    for i in range(len(user_list)-1):
        if user_list[i] < user_list[i+1]:
            continue
        else:
            return 'Is not sorted from lower to higher'
    return 'Is sorted from lower to higher'
print(check_if_ordered())

# #17 dado un numero natural mostraR EL MAYOR DE SUS DIGITOS

# def show_higher_digit(number : int)  -> int:

#     check_number : int = is_numeric_validation(number)
#     return f'Higher digit is: {max(number)}.' 

# print(show_higher_digit(number))
#18 dados 3 numeros naturales :A, B y C; mostrar los multiplos de A menores que B que no sean divisores de C

# def no_idea_name(numA : int, numB: int, numC: int):

#     result : list = []
#     for i in range(1, numA):
#         if numA % i == 0 and numA / i < numB and numC % i != 0:
#             result.append(i)
            
#     return f'Result: {result} '

# print(no_idea_name(80,70,35))

# # 19 dado un numero natural , calcular swu factorial

# def factorial(num : int) -> int:
#     result : int = 1
#     for i in range(1, int(num)+1):
#         result *= i
#     return result

# print(factorial(number))

#dados 3 digitos , generar y mostrar el mayor numero natural que puee escribirse con ellos

def write_higher_num ():
    numA = input('Insert number A: ')
    numB = input('Insert number B: ')
    numC = input('Insert number C: ')

    check_numA = is_numeric_validation(numA)
    check_numB = is_numeric_validation(numB)
    check_numC = is_numeric_validation(numC)

    if check_numA and check_numB and check_numC:
        all =numA+numB+numC
        all_sorted = sorted(all, reverse= True)
        return f"Higher number can be writen is : {''.join(all_sorted)}"
        
print(write_higher_num())

