# Ejercicio 1 : Crear una clase llamada Persona donde sus atriutos van a ser :

# Atributos : nombre, Edad , DNI
# Y los métodos ; - mostrarEdad(): devuelve la edad de la persona
#                 - esMayorDeEdad() : devuelve Tue si es mayor igual a 18
# Realizar su respectivo constructor , métodos y atributos.

class Persona:
  #define constructor con sus atributos
  def __init__(self, nombre, edad, dni) -> None:
    self.nombre = nombre
    self.edad = edad
    self.dni = dni
  # define métodos
  def mostrarEdad(self):
    return self.edad

  def esMayorDeEdad(self):
    return self.edad >= 18

# ejercicio 2 : Crear una clase llamada calcualdora donde no va a tener ninguna clase pero si los siguientes métodos:
#   Métodos
#        - sumar(n1,n2)
#        - restar(n1,n2)
#        - dividir(n1,n2)
#        - multiplicar(n1,n2)

class Calculator():
    """ Calculator has four methos to solve basic math operation """


    def sumar(self, num_one, num_two) -> int:
        """ Recibe dos numeros y retorna la suma de los mismos"""
        return num_one + num_two

    def restar(self, num_one, num_two) -> int:
        """ Recibe dos numeros y retorna la rests de los mismos"""
        return num_one - num_two

    def dividir(self, num_one, num_two) -> int:
        """ Recibe dos numeros y retorna el cociente de los mismos"""
        return num_one / num_two
    def multiplicar(self, num_one, num_two) -> int:
        """ Recibe dos numeros y retorna el proiducto de los mismos"""
        return num_one * num_two

calculator_one = Calculator()

# print(calculator_one.sumar(5,10))

# Ejercicio 3 :
#  Crear una clase llamada Lista de Tareas que no recibe argumento en su construcor, pero tendrá un argumento definido como una lista y contendrá los siguietes métodos :
    # Métodos :
    # - MostrarTareas()
    # - agregarTarea(tarea)
    # - quitarTarea(tarea)

class TodoList:
    """ A todoList"""
    list = []

    def show_tasks(self):
        """ Returns list of tasks"""
        return self.list

    def add_task(self, task: str)-> None:
        """ Recives a task (as str) and returns void"""
        self.list.append(task)
        print(f'{task} added sucessfully')

    def remove_task(self, task: str)-> None:
        """ Recives a task (as str) and erase it from list"""

        if task in self.list:
            self.list.remove(task)
            print(f'{task} removed')
        print('Task not found')



# mis_tareas = TodoList()

# print(mis_tareas)
# print(mis_tareas.show_tasks())
# print(mis_tareas.add_task('Leer'))
# print(mis_tareas.add_task('estudoar'))
# print(mis_tareas.add_task('Cantar'))
# print(mis_tareas.show_tasks())
# print(mis_tareas.remove_task('Leer'))
# print(mis_tareas.show_tasks())
# print(mis_tareas.remove_task('SAcara la basura'))
# print(mis_tareas.show_tasks())


# Ejercicio 4: Crear un clsase llamada Revertir, que recibirá una lista de palabras y las trasformará en un string con las palabras invertidas :
#["hola", " como", "estas"] --> "estas como hola"

# atributos = - lista_de_palabras

# MEtodos :
# - revertir
# - mostrar_frase

class Revert:
    """ recibes a list and returns a string"""
    def __init__(self, words_list) -> None:
       self.words_list = words_list

    def revert(self):
        """ returns the list reversed"""
        list = self.words_list[::-1]
        self.words_list = list
        return self.words_list
    
    def show_phrase(self):
        """ transforms the reverted list i a sring and returns it"""
        return ' '.join(map(str, self.words_list))


new_list = Revert(['Hola', 'soy', 'Lu', 1, 2, 3])
print(new_list.revert())
print(new_list.show_phrase())
