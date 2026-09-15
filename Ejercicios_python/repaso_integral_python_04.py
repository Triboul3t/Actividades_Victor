# ============================================
# REPASO INTEGRAL DE PYTHON
# Material de consulta - todo lo visto hasta ahora
# ============================================

# --------------------------------------------
# 1. VARIABLES Y TIPOS DE DATO
# --------------------------------------------
nombre = "Juan"          # texto (string)
edad = 25                 # numero entero (int)
estatura = 1.75            # numero decimal (float)
es_estudiante = True        # booleano (True o False)

print(nombre, edad, estatura, es_estudiante)


# --------------------------------------------
# 2. INPUT Y CONVERSION DE TIPOS
# input() siempre devuelve texto, por eso hay que 
# convertir si vamos a hacer calculos
# --------------------------------------------
edad_texto = input("Cuantos anios tienes?: ")   # queda como texto
edad_numero = int(input("Cuantos anios tienes?: "))    # se convierte a entero
precio = float(input("Precio: "))                # se convierte a decimal


# --------------------------------------------
# 3. F-STRINGS - insertar variables dentro de un texto
# --------------------------------------------
print(f"Hola {nombre}, tienes {edad} anios")


# --------------------------------------------
# 4. CONDICIONALES
# --------------------------------------------
edad = 20

if edad < 12:
    print("Eres nino")
elif edad < 18:
    print("Eres adolescente")
else:
    print("Eres adulto")

# and: se cumple SOLO si AMBAS condiciones son verdaderas
if edad >= 18 and es_estudiante:
    print("Eres adulto y estudiante")

# or: se cumple si AL MENOS UNA condicion es verdadera
if edad < 12 or edad > 65:
    print("Aplica descuento especial")


# --------------------------------------------
# 5. WHILE - repetir mientras se cumpla una condicion
# --------------------------------------------
contador = 0
while contador < 3:
    print(f"Vuelta numero {contador}")
    contador = contador + 1


# --------------------------------------------
# 6. LISTAS - guardar varios datos juntos
# --------------------------------------------
frutas = ["manzana", "pera", "uva"]

print(frutas[0])         # accede al primer elemento -> "manzana"
frutas.append("sandia")   # agrega al final
print(len(frutas))        # cuenta cuantos elementos hay
print(sum([10, 20, 30]))  # suma los elementos (solo con numeros)


# --------------------------------------------
# 7. FOR - recorrer una lista
# --------------------------------------------
for fruta in frutas:
    print(fruta)

# enumerate() da la posicion y el contenido a la vez
for i, fruta in enumerate(frutas):
    print(i, fruta)


# --------------------------------------------
# 8. LIST COMPREHENSION - forma corta de crear listas
# --------------------------------------------
numeros = [1, 2, 3, 4, 5]

# forma larga
cuadrados_largo = []
for n in numeros:
    cuadrados_largo.append(n**2)

# forma corta (hace lo mismo)
cuadrados_corto = [n**2 for n in numeros]

# con condicion
pares = [n for n in numeros if n % 2 == 0]


# ============================================
# EJERCICIOS PARA PRACTICAR
# ============================================

# Ejercicio 1 (variables + f-strings)
nombre = "Julian"
edad = 22
ciudad = "Medellin"
print(f"Me llamo {nombre}, tengo {edad} años y vivo en {ciudad}")

# Ejercicio 2 (condicionales)
nota = float(input("Ingresa tu nota (0 a 5): "))
if nota >= 3:
    print("Aprobado")
else:
    print("Reprobado")

# Ejercicio 3 (while)
numeros_ingresados = []
while True:
    entrada = input("Ingresa un numero (o escribe 'salir' para terminar): ")
    if entrada == "salir":
        break
    numeros_ingresados.append(entrada)
print(f"Escribiste {len(numeros_ingresados)} numeros")

# Ejercicio 4 (listas + for)
precios = [15000, 8000, 22000, 35000, 5000]
for precio in precios:
    if precio > 20000:
        print(precio)

# Ejercicio 5 (list comprehension)
edades = [15, 22, 17, 30, 12, 19]
mayores_edad = [edad for edad in edades if edad >= 18]
print(mayores_edad)