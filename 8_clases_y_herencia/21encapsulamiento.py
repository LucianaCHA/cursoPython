# encapsulaminto, no se usa demasiado porque no se puede hacer verdaeramente

# para simular el comportamiento se antepone al nombre del método o aributo dos guiones bajos

class Prueba:

  __atributo_privado = 'Algo'

  def mostrar_atributo_privado(self):
    print(self.__atributo_privado)

  def  __metodo_privado(self):
    print('Método encapsulado')

  def ejecutar_metodo_privado(self):
    self.__metodo_privado()

prueba = Prueba()

# prueba.__atributo_privado # lanza un error AttributeError: 'Prueba' object has no attribute '__atributo_privado'

# prueba.mostrar_atributo_privado() # Algo 

# prueba.__metodo_privado() # AttributeError: 'Prueba' object has no attribute '__metodo_privado'

prueba.ejecutar_metodo_privado()  # imprime Método encapsulado 