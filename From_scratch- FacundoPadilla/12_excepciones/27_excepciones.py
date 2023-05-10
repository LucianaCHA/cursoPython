# comprensión de listas

# 1. Crear una lista de números del 1 al 10
# 2. Crear una lista de números pares del 1 al 10
# 3. Crear una lista de números impares del 1 al 10
# 4. Crear una lista de números del 1 al 10 elevados al cuadrado
# 5. Crear una lista de números del 1 al 10 elevados al cubo
# 6. Crear una lista de números del 1 al 10 elevados a la potencia n
# 7. Crear una lista de números del 1 al 10 elevados a la potencia n
# 8. Crear una lista de números del 1 al 10 elevados a la potencia n
# 9. Crear una lista de números del 1 al 10 elevados a la potencia n
# 10. Crear una lista de números del 1 al 10 elevados a la potencia n
a = []
for i in range(1, 11):
    a.append(i)
print(a)

## Lo anterior se puede reducir a una sola línea de código por medio de la comprensión de listas

a = [i for i in range(1, 11)] # primero uso el iterador
print(a)

# se pueden usar condicionales
a = [i if i % 2 == 0 else i*3 for i in range(1, 11) ]  # primero uso el iterador, luego la condición y fialemnte defino el rango
print(a)

## se recomienda el uso de comprensión de listas en lugar de bucles for cuando se trabaja con listas y cuandp se requiere una sola línea de código , en cambio si dboi ejecutar varias líneas de código o si se requiere un bucle for anidado se recomienda el uso de bucles for tradicionales

####==========================####

#genradores de listas
# optimización de la memoria en python por medio de la comprensión de listas

def generador():
    num = 0
    while (True):
        yield num # yield es una palabra reservada que permite generar un generador, cede el control de la ejecución de la función y se queda esperando a que se vuelva a llamar, cuando se vuelve a llamar la función se ejecuta desde el punto en el que se quedó, es decir, se ejecuta desde el yield y no desde el principio de la función. de esta manera se optimiza la memoria ya que no se almacena en memoria la lista completa, sino que se va almacenando en memoria cada elemento de la lista conforme se va ejecutando la función
        num += 1

# en general se usa el generador cuando se requiere una lista muy grande y se requiere optimizar la memoria, de todos modos se recomienda usar un limite para que no se genere una lista infinita

def generador_limite(limite):
    num = 0
    while (num < limite):
        yield num 
        num += 1

a = generador()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
