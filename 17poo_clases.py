#POO, programcacion Orientada a objetos
#En lugar de logicas y fiunciones se vale además de objetos

# En python estos objetos son CLASES y las mismas pueden INSTANCIARSE

# Además las mismas cuentan con
#                 MÉTODOS (Qué acciones puede realizar )
#                 ATRIBUTOS (Características)

# Por ej:

# para la clase PERSONA------ JUAN es una instancia
#                      |------ MARIA es otra intancia

# Sintaxis para crear una clase

class Persona_ejemplo1:
  # init es u método mágico, eestá pensadas solo para ser usada por python y no por el dev
  # init sewria el contructor de clase y con él se establecen los atributos de la misma

  # self puede entenderse literal como 'así mismo' equivalentre al ths en js
  # significa que para obtener los valores en el contructor se refiere o utiliza el 'self'.
  # self es unico de cada objeto

  def __init__(self, argumentos) -> None:
    self.primer_argumento = argumentos[0]
    self.segundo_argumento = argumentos[1]

# Luego se definen los métods

  def hablar(self):
    ...
  def cantar(self):
    ...
  def bailar(self):
    ...
  def saludar(self):
    ...
  def correr(self):
    ...

#agregando atributos y métodos a la clase

class Persona_ejemplo2:
  def __init__(self, color_pelo, altura, tipo_de_voz) -> None:
    self.color_pelo = color_pelo
    self.altura = altura
    self.tipo_de_voz = tipo_de_voz

# Luego se definen los métods

  def obtener_color_pelo(self):
    return self.color_pelo

  def cantar(self):
    ...
  def bailar(self):
    ...
  def saludar(self):
    ...
  def correr(self):
    ...

# Intanciar clase=>>>

juan = Persona_ejemplo2("castaño", 1.70, " grave")
maria = Persona_ejemplo2("negro", 1.50, " aguda")

# 'llamando' atributo y métodos

juan.color_pelo # devuelve castaño / self.color_pelo

juan.obtener_color_pelo() # retorna cawstaño