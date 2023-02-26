# copiar objetos

class Prueba: # dada una clase Prueba
  pass

prueba1 = Prueba() # prueba1 es una instancia de la clase prueba
prueba2 = prueba1 # no puede reasignarse a una nueva variable

# prueba1 y prueba2 hacen referecia al mismo objeto, misma diorección de memoria. Si hago un cambio en prueba1 se refleja tambien en prueba2  pues son lo mismo

# paracopiar el objeto y que realmente sean dos distintos 

from copy import copy

prueba1b = Prueba() # prueba1b es una instancia de la clase prueba
prueba2b = copy(prueba1) # esto si genera una copia del objeto a una nueva referencia en memoria

#para copiar diccionarios, usar deepcopy()