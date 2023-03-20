# definir valorespreestablecidos para las rutas y documentarlas con swagger

from fastapi import FastAPI, Path, Query
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
    {'titulo': 'titulo 4', 'descripcion': 'descripcion 4'},
    {'titulo': 'titulo 5', 'descripcion': 'descripcion 5'},
    {'titulo': 'titulo 6', 'descripcion': 'descripcion 6'},
]


from copy import copy

@app.get('/items/')
async  def get_items(indice : int= 0, cantidad : int = 5):
    return indice, cantidad, fake_db[indice: indice + cantidad]

#parametros opcionales
@app.get('/items/{indice}')
async def get_item(indice: int, mayus: Optional[bool]= False, mius: Optional[bool]= False):
    if mayus:
        copia = copy(fake_db[indice])
        print(copia["descripcion"].upper())
        return  copia["descripcion"].upper()
    if mius:
        copia = copy(fake_db[indice])
        return  copia["descripcion"].lower()
    return fake_db[indice]
    


#parametros requeridos 
@app.get("/requeridos")
async def requeridos(requerido: str): # si pongo un valor por defecto no es requerido, en cambio si no pongo nada es requerido y debo enviarlo
    return {'requerido': requerido}


# metadatos en query parameters (muchos son para la doc de swagger)
from fastapi import Query
from typing import Optional, List

@app.get("/lista")
async def lista_query(q: Optional[List[str]]= Query(
    ['uno', 'dos'],
    alias="Query string",
    description="Lista de valores",
    deprecated=True, # si esta en true no se debe usa el metodo   
    
    )):
    query_items = {"q": q} # q es el alias del parametro
    return query_items


# validadoes query parameters, aca vemos los tipos de validaciones que podemos hacer con query parameters

from fastapi import Query

## validaciones de query parameters sirve para validar los parametros que se envian en la url en el query string

@app.get("/validaciones")
async def validaciones(
    q: Optional[str] = Query(
    None, #default value , aca es como que no es requerido y query parsea el none como null, => /validdaciones => q = null
    #si escribo algo en la url => /validaciones?query=algo => q = algo
    # lo parsea a string xq es un string 
    min_length=3, # minimo de caracteres que puede tener el string
    max_length=50, # maximo de caracteres que puede tener el string 
    regex="^pepe", # expresion regular que debe cumplir el string
    # size: float = Query(..., gt=0, le=10.5), # gt = greater than, le = less than
    )):
    results = {"q": q} 
    return results


# multiples valores o lista de valores en query parameters
from fastapi import Query
from typing import Optional, List

@app.get("/lista-query")
async def multiples_valores_query(q: Optional[List[str]]= Query([])):# pra que la [documenatcio interactiova muestre correctamente los valores de la lista debo poner una lista vacia como default value
    query_items = {"q": q}
    return query_items


# valores por defecto en query parameters del tipo lista

from fastapi import Query
from typing import Optional, List

@app.get("/lista-query-def")
async def multiples_valores_query_def(q: Optional[List[str]]= Query(["uno", "dos"])):
    query_items = {"q": q}
    return query_items


# List de typing vs list de python 

# La differecia principal es que List solo soorta un unicvo type, mientras que list de python soporta listas dinámicas de cualquier tipo


##########################################################################333
# Path parameters

# los path parameters son los parametros que se envian en la url despues de la ruta, por ejemplo en la ruta /items/1 el 1 es un path parameter

# los path parameters son requeridos por defecto, si no se envian se genera un error

# los path parameters se definen en la ruta con llaves {parametro}

# los path parameters se definen en la funcion con el mismo nombre que en la ruta


@app.get("/ruta/{parametro}")
async def funcion(parametro: int = Path(...
                                        # min_length=3, max_length=50, regex="^pepe"
)):
    return {"parametro": parametro}

# definiendo query parameters con path parameters en la vista
# python espera que los valores por default estén definidos al finl de la lista de parametros

@app.get("/path/{item}")
async def funcion_obtener(
        # q: str, #esto así rompe porque se toma como un parametro requerido
        q: Optional[str] = Query(None),
        item: int = Path(...)
        ):
    results = {"item": item, "q": q}
    return results