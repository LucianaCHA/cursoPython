def suma(num1 : int, num2 : int) -> int:
    if(num1 is None or num2 is None):
        raise TypeError("num1 y num2 no pueden ser None")
    if(not isinstance(num1, int) or not isinstance(num2, int)):
        raise TypeError("num1 y num2 deben ser de tipo int")
    return num1 + num2









#mockear un api
# pip install requests-mock

import requests, json

datos = requests.get('https://www.freetogame.com/api/games')

with open('data.json', 'w') as file:
    file.write(json.dumps(datos.json()))

# data.json es un archivo json con los datos de la api
# mesirve para mockear una api

def obtener_juegos():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data


def una_funcion():
    return 1

def ejecutar_funcion():
    return una_funcion()