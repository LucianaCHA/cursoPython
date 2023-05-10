#Secuencias : listas, tuplas, cadenas, bytes, range (#estrutura con orden determinista)

lista = [1,2,3,4,0]
print(lista)

#Colecciones : diccionarios, sets

conjunto = {1,2,3,4,0} # ordena los elementos y elimina los duplicados
diccionario = {"key":1, "key":2, "c":3, "d":4, "e":0}
print(conjunto)
print(diccionario)



#######################################
## secuencias y coleccions con pydantic

from typing import Any, Sequence, Dict
from pydantic import BaseModel, StrictStr

class Classe(BaseModel):
    secuencia: Sequence = None
    coleccion: Dict[StrictStr, Any] = None # Any es un tipo de dato que permite cualquier tipo de dato

print(
        Classe(secuencia=[1,2,3]).secuencia,
    Classe(secuencia=[1,4,0,3]).secuencia,
    # Classe(secuencia={'key':'value'}).secuencia # no es una secuencia pdispar un error 
    )

#############################333
# generdores pydantic

from typing import Iterable
from pydantic import BaseModel, StrictStr

class Generador(BaseModel):
    generador: Iterable[int]

def generador_numeros():
    i = 0
    for i in range(10):
        yield i

        i += 1
        print(i)

gen1 = Generador(generador=generador_numeros())

for i in gen1.generador:
    if i == 5:
        break

## validar que devolvio u generdor pydntic

#retomo el ejemplo ANTERIOR
from pydantic import validator

class GeneradorValidado(BaseModel): # declaro una clase que hereda de BaseModel como siempre
    generador: Iterable[int]

    @validator('generador') # decorador que permite validar el campo    
    def validar_generador(cls, generador): # el método recibe el valor del campo
        valor = next(generador) # obtengo el primer valor del generador
        
        if isinstance(valor, int): # si el valor es un entero todo bien
            print("El valor es un entero")
        else:
            raise TypeError("El valor no es un entero")
    
def generador_numeros_validado():
    k = 'k'
    for k in range(10):
        yield k

        k += 1
        print(k)

gen2 = GeneradorValidado(generador=generador_numeros_validado())

for i in gen2.generador:
    if i == 5:
        break
