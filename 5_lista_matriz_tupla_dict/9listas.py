#una lista es una coleccionde elementos dinámica, es decir puede variar su tamaño
color = 'rojo'
lista = [1,2,3,'hola', color, True ]

print('Longitud lista:', len(lista))
#posicion

print('el primer elemento es: ', lista[0])
print('el ultimo elemento es: ', lista[len(lista)-1])

#slicing, señalo las posiciones con negativosy con los dos puntos
print('el primer elemento es: ', lista[-6])
print('los dos primeros elementos son: ', lista[0:2])
print('los dos ultimos elementos son: ', lista[-2:])
print('todos menos el primero: ', lista[1:])
print('todos menos el ultimo: ', lista[:-1])
print('todos', lista[:])
print('todos menos el primero y el ultimo: ', lista[1:-1])

# dar reversa a una lista
print('lista original: ', lista)

print('reversa; ', lista[::-1])


#propiedades de las listas

texto = ['hola', 'mundo', 'python']

for palabra in texto:
    print(palabra + ' ', end = '')

print('\n ***************')

for palabra in range(len(texto)):
    print(texto[palabra] + ' ', end = '')

#ordenar una lista

lista_desordenada = [1,12,3,14,5,61,7,28,9,10]
lista_ordenada = lista_desordenada.sort()

print('lista desordenada: ', lista_desordenada)

lista_sorted = sorted(lista_desordenada)
lista_sorted_reversed= sorted(lista_desordenada, reverse = True)
print('sorted reversed: ', lista_sorted_reversed)
print('lista sorted: ', lista_sorted)
print('lista sorted al reves: ', lista_sorted[::-1])


#agregar elementos a una lista
#append, agrega un elemento al final de la lista
lista_vacia =[]
lista_vacia.append(1)
lista_vacia.append(2)
print('lista vacia: ', lista_vacia)
#insert, agrega un elemento en la posicion que le indiquemos
lista_vacia.insert(0, 0) # recibe dos parametros, la posicion y el elemento
print('lista vacia: ', lista_vacia)

#extend, agrega una lista al final de la lista
lista_vacia.extend([3,4,5])
print('lista vacia: ', lista_vacia)

#eliminar elementos de una lista
#pop, elimina el ultimo elemento de la lista si n recibe paramétro, si lo recibe eliminará el elementos de la posiión indicada. Además retorna el elemento eliminado

lista_vacia.pop()
print('lista vacia: ', lista_vacia)

lista_vacia.pop(1)
print('lista vacia: ', lista_vacia)

#remove, elimina el elemento que le indiquemos
lista_vacia.remove(3)
print('lista vacia: ', lista_vacia)


#del se puede usar para eliminar un elemento de una lista o para eliminar la lista completa 
lista = [1,2,3,4,5]
del lista[0]
print('del el 0: ', lista_vacia)
# del lista_vacia
# print('lista vacia eliminada: ', lista_vacia)

#clear, elimina todos los elementos de la lista
lista_vacia.clear()
print('clear lista vacia: ', lista_vacia)


# modificar elementos de una lista

lista = [1,2,3,4,5]
lista[0] = 0
print('lista modificada: ', lista)

#buscar elementos en una lista
#in, retorna true si el elemento se encuentra en la lista, false en caso contrario
lista = [1,2,3,4,5]

print('in 1: ', 1 in lista)
print('in 6: ', 6 in lista)
print('buscando con index:',lista.index(1))