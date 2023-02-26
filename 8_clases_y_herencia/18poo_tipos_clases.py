# clases abstractas => no pueden ser instancidas se usan para herencia 
# sirven de base para clases concretas que cuentan con atributos y métodos definidos

# ej:
# Clase Abstracta Animal (hay muchos animales pero podemos buscar atributos y métodos comunes a todos)

# ejmplos , la idea es evitar repetir usando herencia
# class Animal:

#   def comer(self):
#     ...
#   def respirar(self):
#     ...

# class Ave:
#   def comer(self):
#     ...
#   def respirar(self):
#     ...
#   def volar(self):
#     ...

# class Conejo:
#   def comer(self):
#     ...
#   def respirar(self):
#     ...
#   def saltar(self):
#     ...

# Lo anterior queda como:

class Animal:

  def comer(self):
    ...
  def respirar(self):
    ...

class Ave(Animal): # Ave hereda todos los metodos de animal
  def volar(self):
    ...

class Conejo(Animal):
  def saltar(self):
    ...



