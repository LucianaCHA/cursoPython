# algo = 'algo'
# type(algo) # indica que tipo de dato es la variable

# isinstance(candidata, clase) # devuelve bool
# issubclass(candidata, clase) # indica s la canddata hereda de la clase

# MRO Méthod Resoluton Order

class Abuelo:
  def saludar(self):
    print('Soy el abuelo')

class Padre(Abuelo):
  def saludar(self):
    print('Soy el padre')

class Madre(Abuelo):
  def saludar(self):
    print('Soy la madre')

class Hijo(Padre, Madre):
  def saludar(self):
    # super toma para herencia la primer clase, por eso no sirve para herencia multiple
    super(Hijo, self).saludar()

hijo = Hijo()

hijo.saludar()