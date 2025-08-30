def estacion():
    mesxdias = {
        "enero": 31, "febrero": 29, "marzo": 31,
        "abril": 30, "mayo": 31, "junio": 30,
        "julio": 31, "agosto": 31, "septiembre": 30,
        "octubre": 31, "noviembre": 30, "diciembre": 31
    }

    mes = input("Ingrese el mes (ejemplo: marzo): ").lower()
    dia = int(input("Ingrese el día: "))

   
    if mes not in mesxdias:
        print("Error: El mes ingresado no es válido.")
        return

    if dia < 1 or dia > mesxdias[mes]:
        print(f"Error: El mes {mes} no tiene {dia} días.")
        return

    if (mes == "marzo" and dia >= 21) or (mes in ["abril", "mayo"]) or (mes == "junio" and dia <= 20):
        estacion = "Primavera"
    elif (mes == "junio" and dia >= 21) or (mes in ["julio", "agosto"]) or (mes == "septiembre" and dia <= 20):
        estacion = "Verano"
    elif (mes == "septiembre" and dia >= 21) or (mes in ["octubre", "noviembre"]) or (mes == "diciembre" and dia <= 20):
        estacion = "Otoño"
    else:
        estacion = "Invierno"

    print(f"Para el día {dia} del mes {mes} estaríamos en {estacion}.")

estacion()
