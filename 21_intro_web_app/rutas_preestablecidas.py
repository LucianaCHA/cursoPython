# definir valorespreestablecidos para las rutas y documentarlas con swagger

from fastapi import FastAPI
from enum import Enum

class ModelLenguajes(str, Enum):
    python = 'python'
    java = 'java'
    javascript = 'javascript'
    golan = 'golan'


app = FastAPI()

@app.get('/lenguajes/{lenguaje}')
async def lenguajes_descripcion(lenguaje: ModelLenguajes):
    if lenguaje == ModelLenguajes.python:
        return {'lenguaje': lenguaje, 'descripcion python': 'lenguaje de programacion'}
    elif lenguaje == ModelLenguajes.java:
        return {'lenguaje': lenguaje, 'descripcion Java': 'lenguaje de programacion'}
    elif lenguaje == ModelLenguajes.javascript:
        return {'lenguaje': lenguaje, 'descripcion js': 'lenguaje de programacion'}
    elif lenguaje == ModelLenguajes.golan:
        return {'lenguaje': lenguaje, 'descripcion golan': 'lenguaje de programacion'}


####  query parameters

from typing import Optional

fake_db = [
    {'titulo': 'titulo 1', 'descripcion': 'descripcion 1'},
    {'titulo': 'titulo 2', 'descripcion': 'descripcion 2'},
    {'titulo': 'titulo 3', 'descripcion': 'descripcion 3'},
]


@app.get('/items/')
async  def get_items(indice : int= 0, cantidad : int = 20):
    return indice, cantidad, fake_db[indice: indice + cantidad]


@app.get('/items/{indice}')
async def get_item(indice: int, mayus: Optional[bool]= False, mius: Optional[bool]= False):
    if mayus:
        return fake_db[indice].upper()
    elif mius:
        return fake_db[indice].lower()
    else:
        return fake_db[indice]