from fastapi import FastAPI, Request, Response
from typing import List, Dict, Any


# app = FastAPI()

# @app.get('/') # el metodo 
# async def index(): # la corutina/ vista 
#     return {'key': 'value'}

# @app.post('/post')
# async def post_info(request: Request):
#     data = await request.json()
#     return data
app = FastAPI()

Listamodelo = List[Dict[Any, Any]]

lista_usuarios : Listamodelo = []

id = 1

def modificar_usuario(id: int, usuario_data: Dict[Any, Any]):
    for usuario in lista_usuarios:
        if usuario['id'] == id:
            usuario.update(usuario_data)
            return usuario
        else:
            return 'usuario no encontrado'
    return None

# @app.get('/')
# async def mostrar_usuarios():
#     return lista_usuarios
# puedo modificar los status code

@app.get(path= '/', status_code=200)
async def mostrar_usuarios():
    if lista_usuarios:
        return lista_usuarios
    return Response(content = 'no hay usuarios', status_code=404)

@app.post('/crear_usuario')
async def crear_usuario(request: Request):
    global id
    nuevo_usuario = await request.json()
    if nuevo_usuario:
        nuevo_usuario['id'] = id
        id += 1
        lista_usuarios.append(nuevo_usuario)
        return nuevo_usuario
    return {'error': 'no se pudo crear el usuario'} 

@app.put('/actualizar_usuario/{id}')
async def actualizar_usuario(id : int, request: Request):
    usuario = await request.json()
    if usuario:
       return modificar_usuario(id, usuario)
    return {'error': 'no se pudo actualizar el usuario'}

@app.patch('/actualizar_usuario/{id}')
async def actualizar_usuario_patc(id : int, request: Request):
    usuario = await request.json()
    if usuario:
       return modificar_usuario(id, usuario)
    return {'error': 'no se pudo actualizar el usuario'}

@app.delete('/eliminar_usuario/{id}')
async def eliminar_usuario(id: int):
    for usuario in lista_usuarios:
        if usuario['id'] == id:
            lista_usuarios.remove(usuario)
            return {'mensaje': 'usuario eliminado'}
    return {'error': 'no se pudo eliminar el usuario'}
#####################


# from fastapi import FastAPI, Request, Response
@app.get(path='/prueba/parametros/{id}')
async def prueba_parametros(id: int):
    return {'id': id}
### swagger 

