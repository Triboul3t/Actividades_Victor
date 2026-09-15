#===========================
#   SISTEMA DOMICILIOS
#===========================

#Bucle infinito que mantiene el programa corriendo hasta que el usuario decida salir
while True:
#Imprime el encabezado del sistema cada vez que se repite el ciclo
    print("\n"+"="*30)
    print("SISTEMA DOMICILIOS".center(30))
    print("="*30)
    
    #Pide al usuario la distancia en kilómetros y la convierte a número decimal (float)
    distancia_km = float(input("\nIngrese la distancia en Km: "))
    
    #Si la distancia es de 3 km o menos, el domicilio cuesta 3000
    if distancia_km <= 3:
        costo_domicilio = 3000
    #Si la distancia está entre 3 y 8 km, el domicilio cuesta 8000
    elif distancia_km > 3 and distancia_km <= 8:
        costo_domicilio = 8000
    #Si la distancia es mayor a 8 km, no se hace el domicilio (costo queda en 0)
    else:
        costo_domicilio = 0

    #Si el costo quedó en 0, significa que está fuera del área de cobertura
    if costo_domicilio == 0:
        print(f"Por fuera del area - No hay domicilio")
    #Si tiene un costo válido, se muestra el valor del domicilio
    else:
        print(f"\nCosto domicilio = ${costo_domicilio}")
    
    #Pregunta si el usuario quiere calcular otro domicilio
    continuar = input("\nContinuar? (Y/N): ")
    #Convierte la respuesta para que solo la primera letra quede en mayúscula (acepta "y" o "Y")
    continuar = continuar.capitalize()

    #Si la respuesta es "Y", el ciclo vuelve a empezar
    if continuar == "Y":
        continue
    #Si la respuesta es cualquier otra cosa, se rompe el ciclo y el programa termina
    else:
        break

#Mensaje de despedida cuando el usuario decide salir del sistema
print("\n"+"="*30)
print("Apagando sistema...".center(30))
print("="*30)