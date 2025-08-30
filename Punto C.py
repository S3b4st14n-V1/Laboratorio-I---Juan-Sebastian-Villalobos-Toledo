import numpy as np

def matriz_y_transpuesta():
    N = int(input("Ingrese el tamaño de la matriz cuadrada (N): "))
    matriz = []

    for i in range(N):
        fila = []
        for j in range(N):
            valor = int(input(f"Ingrese el valor para la posición ({i},{j}): "))
            fila.append(valor)
        matriz.append(fila)

    matriz = np.array(matriz)

    print("\nMatriz original:")
    print(matriz)

    transpuesta = matriz.T

    print("\nMatriz transpuesta:")
    print(transpuesta)

matriz_y_transpuesta()
