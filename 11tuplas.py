#las tuplas son listas inmutables no es posible reasignar valores

tupla = (1,2,3,4,5,6,7,8,9,10)
print('tupla: ', tupla)

#posicion
print('el primer elemento es: ', tupla[0])
print('el ultimo elemento es: ', tupla[len(tupla)-1])

#even wen is not reasignable, we can transform the tuple in a list

print('tupla before change: ', tupla)
lista = list(tupla) #turn the tuple in a list
lista[0] = 'hola' #make the change
tupla = tuple(lista) #turn the list in a tuple
print('tupla after change: ', tupla)