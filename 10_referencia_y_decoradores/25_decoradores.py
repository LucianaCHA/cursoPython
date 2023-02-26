def decorador(funcion):
    def envoltura():
        print("Antes de la función")
        funcion()
        print("Después de la función")
    return envoltura

@decorador
def saludo():
    print("Hola mundo")

saludo()


# ejemplo mas complejo

class A:
    def __init__(self, nombre) -> None:
        self._nombre = nombre

    @property # decorador nativo de python para convertir un metodo en atributo
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, argumento):
        print("Se está cambiando el nombre")
        self._nombre = argumento

    @nombre.getter
    def nombre(self):
        print("Se está accediendo al nombre")
        return self._nombre
      
    @nombre.deleter
    def nombre(self):
        print("Se está borrando el nombre")
        del self._nombre

a = A("Juan")
print(a.nombre)

