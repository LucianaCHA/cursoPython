# función open 

texto = open("texto.txt", "r")

print(texto) #3imprime tipo archivo , codificcación
print(texto.read())##esto si imprie a consola el contenido del archivo
print(texto.readlines())##esto  imprie a consola el contenido del archivo
# El método anterior consume memoria guardando lo que impremi
#como alternativa print(texto.readline()) carga, lee e imprime en forma iterativa 

# wrie no verifica si el archivo, si existe soibrescribe
# nombre_de_archivo.write('texto que quiero agregar' )

# nombre_archivo.close() #close permite lierar memoria

#Para evitar da la instruccion close puedo usar la sgte instr

with open("nombre archivo", "w") as alias_archivo:
  alias_archivo.write('nuevo texto que reemplazar a a nombre_archivo o lo creará')
 #si quiero abrir si borrar

  a = open("nombre archivo", "a") # a si no exte el archivbo lo crea, caso contrario appendea lo que escribo
