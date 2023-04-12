from pydantic import BaseModel # pydantic is a data validation library
from fastapi import FastAPI, Path, Query
from typing import Optional


class ModelPerson(BaseModel):
    name: str
    age: int
    email: str

app = FastAPI()

@app.post('/person/create')
async def create_person(person: ModelPerson):# fastApi interprets the body of the request as a JSON or dict and maps it to the ModelPerson
    return person.dict()

# combine path and body parameters
# se usa mucho para actualizar datos
@app.put('/person/update/{id}')
async def update_person(
    person: ModelPerson,
    id: int = Path(...) # buena practi8ca , definir el param por query o ruta
    ):
    return {'id': id, 'person': person.dict()}
    # return {'id': id, **person.dict()}


# combinar request body, query params y path params

@app.put('/person/update2/{id}')
async def update_person2(
    person: ModelPerson,
    id: int = Path(...),
    without_id: bool = Query(False), # query params con la url http://127.0.0.1:8000/person/update2/3?without_id=1 no incluye id en el json
    # query params
    q: str = None
    ):
    if without_id:
        return person.dict()
    return {'id': id, 'person': person.dict(), 'q': q}


#enviar multiples parametros en el body
#  puedeo crear tatos modelos como parametros tenga el body y enviarlos como diccioaris aniidados en el body

class ModelPerson2(BaseModel):
    name: str
    age: int
    email: str
    hobbies: str

class userModel(BaseModel):
    username: str
    password: str

@app.post('/person/create2')
async def create_person2(person: ModelPerson2, user: userModel):
    return {'person': person.dict(), 'user': user.dict()}


# valores singulares en el body
# con valor singular refiere a no enviar un modeolo de pydantic sino un valor simple como un string, int, float, bool, etc para esto usamos una funcion body de fastapi

# para esto la forma es pasarle el tipo de dato que se espera en el body 

from fastapi import Body
@app.post('/person/create3')
async def create_person3(person: str = Body(...)):
    return person

# valores singulares en el body con validacion
# para esto la forma es pasarle el tipo de dato que se espera en el body

from fastapi import Body
@app.post('/person/create4')

async def create_person4(

    person: str = Body(..., min_length=3, max_length=50, regex="^pepe")

    ):
    return person

# multiples valores en el body

from fastapi import Body

@app.post('/person/create5')
async def create_person5(
    param1: str = Body(...),
    param2: str = Body(...),
    param3: int = Body(...),
    ):
    return {'param1': param1, 'param2': param2, 'param3': param3}


#embeber modelos de pydantic en l body

from fastapi import Body

@app.post('/person/create6')
async def create_person6(
    person: ModelPerson = Body(..., embed = True), #es como que declaro el type con el modelo de pydantic y le digo que lo incluya en el body (seria el embed = True    )
    user: userModel = Body(...),
    ):
    return {'person': person.dict(), 'user': user.dict()}

# Validacion de datos en el body con pydantic y fastapi

# usamos Field de pydantic para validar los datos y sumar mas informacion a los parametros de la docu autogenerada

from pydantic import BaseModel, Field

class ModelPerson(BaseModel):
    name: str
    age: int
    email: str = Field(
        default=..., # el valor por defecto
        title="Email", # titulo del campo
        description="Email de la persona", # descripcion del campo
        max_length=50, # longitud maxima del campo
        regex="^.*@.*$", # expresion regular para validar el campo
    )

## lo anteriro se refleja en la documentacion autogenerada

# listas en body 

from typing import List

class Prueba(BaseModel):
    lista: List[str] = []

@app.post('/prueba')
# async def prueba(prueba: Prueba): # asi si no se envia nada en el body se crea una lista vacia, aunque si osi debe recibor  un body si no se envia nada se genera un error

async def prueba(prueba: Prueba = Body(...)): # asi funciona igual pero es una forma mas explicita de decir que se espera un body
    return prueba

from pydantic import BaseModel, Field, HttpUrl

#anidar modelos de pydantic en el body
class Image(BaseModel):
    url: HttpUrl # HttpUrl es un tipo de dato de pydantic que valida que el valor sea una url valida

class Producto(BaseModel):
    nombre: str
    precio: float
    foto : Optional[Image] = {} # el campo es opcional si o recibe nada se crea un diccionario vacio

@app.post('/producto/crear')
async def producto(producto: Producto):
    return producto


# el body serias asi
# {
#   "nombre": "str",
#     "precio": 4,
#     "foto" : {
#       "url":"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.GhhZk37U4KMIgOZIbUrEFgHaEw%26pid%3DApi&f=1&ipt=727d5b43f622b69795064ead8b6ea4ce074caaffe4a20eb0a5db8d922b8c3888&ipo=images"
#     }
# }

# si va asi 
# {
#   "nombre": "str",
#     "precio": 4
# }

# la response es 

# {
#   "nombre": "str",
#   "precio": 4.0,
#   "foto": {}
# }