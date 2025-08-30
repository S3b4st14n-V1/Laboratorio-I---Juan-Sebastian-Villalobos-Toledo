import random
import numpy as np

def matrices():
    N = int(input("Ingrese el tamaño de la matriz cuadrada: "))

    matriz_random = [[random.randint(0, 9) for _ in range(N)]for _ in range(N)] 
    print("\nMatriz aleatoria:")
    for fila in matriz_random:
        print(fila)

    matriz_usuario = []
    print("\nIngrese los valores de su matriz:")
    for i in range(N):
        fila = []
        for j in range(N):
            valor = int(input(f"Valor en ({i},{j}): "))
            fila.append(valor)
        matriz_usuario.append(fila)

    print("\nMatriz ingresada por el usuario:")
    for fila in matriz_usuario:
        print(fila)
    

    suma = [[matriz_random[i][j] + matriz_usuario[i][j] for j in range(N)] for i in range(N)]

    print("\nResultado de la suma:")
    for fila in suma:
        print(fila)

matrices()
