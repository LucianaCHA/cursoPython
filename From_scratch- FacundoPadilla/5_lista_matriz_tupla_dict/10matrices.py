matriz = [[1,2,3,0],[4,5,6,8],[7,8,9,11]]

for fila in matriz:
    print(*fila)

#posicion
print('fila 1 ', matriz[0])
tamani_filas = len(matriz[0])
print('tamanio de las filas: ', tamani_filas)
tamanio_columnas = len(matriz)
print('cantidad de columnas ', len(matriz))

#slicing
print('fila 1 ', matriz[0])
print('fila 1- columna 1', matriz[0][0])