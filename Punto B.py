def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: no se puede dividir entre cero."

def calculadora():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación (suma, resta, multiplicacion, division): ").lower()

    if operacion == "suma":
        print("Resultado:", suma(a, b))
    elif operacion == "resta":
        print("Resultado:", resta(a, b))
    elif operacion == "multiplicacion":
        print("Resultado:", multiplicacion(a, b))
    elif operacion == "division":
        print("Resultado:", division(a, b))
    else:
        print("Operación no válida.")

calculadora()
