#pares key-value

diccionario = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

#posicion
print('posicion a: ', diccionario['a'])

#add elements
diccionario['f'] = 6
print('diccionario: 1 ', diccionario)

diccionario.update({'g':7})
print('diccionario: 2 ', diccionario)

#modify elements

diccionario['a'] = 10
print('diccionario: 3 ', diccionario)

diccionario.update({'a':17})
print('diccionario: 4 ', diccionario)

#get elements

print('elemento a: ', diccionario.get('a')) # if the value does not exist, it returns None

print('elemento a: ', diccionario.get('z', 'no existe')) # if the value does not exist, it returns the second parameter

#delete elements

del diccionario['a']
print('diccionario: 5 ', diccionario)

diccionario.pop('b')
print('diccionario: 6 ', diccionario)

#items
print('items: ', diccionario.items())

#keys
print('keys: ', diccionario.keys())

#values
print('values: ', diccionario.values())

#iterar sobre un diccionario

for key, value in diccionario.items():
	print('key: ', key, 'value: ', value)


