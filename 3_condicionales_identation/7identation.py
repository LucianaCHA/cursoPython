numero : int = int(input("Ingrese un numero: "))

def return_string(numero: int) -> str:
    if numero > 0:
        return "El numero es positivo"
    elif numero < 0:
        return "El numero es negativo"
    else:
        return "El numero es cero"

print(return_string(numero))