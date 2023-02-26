# def paso_por_referencia(objeto):
#     objeto.nuevo_atributo = 'nuevo atributo'

# class Clase:
#     pass

# prueba = Clase()

# paso_por_referencia(prueba)

# print(prueba.nuevo_atributo)

# Segun el del curso lo anterior debería devolver 'nuevo atributo' pero no lo hace. ¿Por qué? Porque el del curso usa python 3.8/ y yo 3.9 ya no se pueden agregar atributos en tiempo de ejecución 


#ejercicio 2 simular plea ebtre dos guerreros con atributos y métodos

# class Guerrero:
# atributos: nombre, vida, ataque, defensa, velocidad
# métodos: atacar, defender, esquivar, mostrarVida

# class Batalla:
# atributos: guerrero1, guerrero2

# ej:
# guerrero1 = Guerrero('Juan', 100, 10, 5, 10)
# guerrero2 = Guerrero('Pedro', 100, 10, 5, 10)

# batalla = Batalla(guerrero1, guerrero2)

class Guerrero:
    def __init__(self, nombre, vida, ataque, defensa, velocidad) -> None:
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad

        print(f'Guerrero {self.nombre} creado con éxito')

    def atacar(self, guerrero):
        guerrero.vida -= self.ataque
        print(f'Guerrero {self.nombre} ataca a {guerrero.nombre} con {self.ataque} de daño')
        guerrero.mostrarVida()

    def defender(self, guerrero):
        guerrero.vida -= self.defensa

    def mostrarVida(self):
        print(f'Guerrero {self.nombre} tiene {self.vida} de vida')
        return self.vida

luchador1 = Guerrero('Juan', 150, 10, 5, 10)
luchador2 = Guerrero('Pedro', 180, 10, 5, 10)

luchador1.atacar(luchador2)


class Lucha:
    def __init__(self, guerrero1, guerrero2) -> None:
        self.guerrero1 = guerrero1
        self.guerrero2 = guerrero2

    def pelear(self):
        while self.guerrero1.vida > 0 and self.guerrero2.vida > 0:
            self.guerrero1.atacar(self.guerrero2)
            self.guerrero2.atacar(self.guerrero1)

        if self.guerrero1.vida > 0:
            print(f'El ganador es {self.guerrero1.nombre}')
        else:
            print(f'El ganador es {self.guerrero2.nombre}')
    

batalla = Lucha(luchador1, luchador2)
batalla.pelear()
