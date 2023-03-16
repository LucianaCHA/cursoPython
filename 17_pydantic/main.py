from pydantic import BaseModel, EmailStr, StrictStr, ValidationError
from typing import List, Optional

class PeopleSchema(BaseModel): # Hereda de BaseModel , por convención se le pone el sufijo Schema
    name: StrictStr # El campo es obligatorio, StrictStr es un tipo de dato que valida que sea un string y no hace casting
    surname: str
    age: int
    email: Optional[EmailStr] = None # El campo es opcional, EmailStr es un tipo de dato que valida que sea un email



person1 = PeopleSchema(name="Juan", surname="Perez", age=20)


print(person1)

## es posible recuperar errores de validación

try:
    person2 = PeopleSchema(name=1, surname="Perez", age="20")
except ValidationError as e:
    print(e.json()) # Imprime el error en formato json


## iterar sobre los campos

class Listas(BaseModel):
    lista_simple: List = None
    lista_typing: List[StrictStr] = None # typing permite definir el tipo de dato que contendrá la lista y reforzar la validación

lista = Listas(lista_simple=[1,2,3], lista_typing=[1,2,3])

print(lista)

