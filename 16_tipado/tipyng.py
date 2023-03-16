from typing import Callable, Dict, List , NoReturn, Optional, Union

# type hinting 

# def return_list() -> list[int]: # declarodo como list(int) returns an error because its referencing to int as a class
#     return [1, 2, 3]

def return_list() -> List[int]: # this is the correct way to declare a list of integers
    return [1, 2, 3]


#################

# typing procedure and functions. A function always returns something, even if it is None , instead a procedure does not return anything

def sum(a: int, b: int) -> int:
    return a + b

def procedure(a: int, b: int) -> NoReturn:
    print(a + b)

# valor = procedure(1, 2) # no retorno nada, pero si lo guardo en una variable, me va a dar un None

# alias de tipos

Vector = List[float] # alias de tipo

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

new_vector = scale(2.0, [1.0, -4.2, 5.4])

class Person:
    pass

People = List[Person] # alias de tipo

def mostrar_lista(lista: People) -> NoReturn:
    for i in lista:
        print(i)


JSONLogin = Dict[str, Union[str, int]] # alias de tipo

login_exaqmple = {
    "username": "admin",
    "password": 1234
}

# typing invocables objets x ej invocable() -> int

def function(other_function: Callable[[str], str], argumento: str) -> str:
    return other_function(argumento)

def funcion1(name : str) -> str:
    return f'Hello {name}'

print(function(funcion1, 'Juan')) ## un ejemplo de objeto invocable es una funcion que recibe otra funcion como parametro y la ejecuta  ##

### typing para opcionales

def optional(a: int, b: Optional[int] = None) -> int:
    if b is None:
        return a
    return a + b

print(optional(1, 2))

def functio (name : str, surname : Optional[str] = '') -> str:
    return f'Hello {name} {surname}'
print(functio('Juan'))
