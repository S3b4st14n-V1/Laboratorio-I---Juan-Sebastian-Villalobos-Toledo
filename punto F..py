def reseñas():
    n = int(input("¿Cuántas reseñas desea ingresar? (mínimo 3): "))
    if n < 3:
        print("Debe ingresar al menos 3 reseñas.")
        return

    reseñas = []  

   
    for i in range(n):
        texto = input(f"Ingrese la reseña {i+1}: ").lower() 
        for p in ".,!?":
            texto = texto.replace(p, "")
        reseñas.append(texto)

    print("\nReseñas procesadas:")
    print(reseñas)

    palabras = " ".join(reseñas).split()

    
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

    print("\nDiccionario de frecuencias de palabras:")
    for palabra, freq in frecuencia.items():
        print(palabra, "→", freq)

   
    top3 = sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)[:3]

    print("\nTop 3 palabras más frecuentes:")
    for palabra, freq in top3:
        print(f"{palabra} → {freq} veces")

reseñas()
