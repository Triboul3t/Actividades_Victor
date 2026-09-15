# ============================================
# EJERCICIOS - Listas en Python
# Escribe tu código debajo de cada enunciado
# ============================================

# --------------------------------------------
# ACTIVIDAD 1: Explica con tus palabras qué hace 
# cada línea, agregando un comentario arriba de cada una
# --------------------------------------------
#La variable de notas se encarga de guardar una lista vacia para llenarla con el input
notas = []
#La segunda variable se encarga de tomar el input y guardarlo.
nota1 = float(input("Ingresa una nota: "))
#Se usa el metodo de append para agregar la nota del input a la lista original.
notas.append(nota1)
#Se usa un print para mostrar las notas agregadas
print(f"Total de notas: {notas}")


# --------------------------------------------
# EJERCICIO 1
# Crea una lista vacía llamada "temperaturas".
# Pide 3 temperaturas al usuario (una por una) y 
# agrégalas a la lista. Al final, imprime la temperatura 
# más alta y la más baja (usa max() y min())
# --------------------------------------------
temperaturas = []

tempt1 = float(input("Ingrese la primera temperatura: "))
tempt2 = float(input("Ingrese la segunda temperatura: "))
tempt3 = float(input("Ingrese la tercera temperatura: "))

temperaturas.append(tempt1)
temperaturas.append(tempt2)
temperaturas.append(tempt3)

print(f"La temperatura mas alta es {max(temperaturas)} y la temperatura mas baja es {min(temperaturas)}")

# --------------------------------------------
# EJERCICIO 2
# Crea una lista con 5 nombres de compañeros.
# Recorre la lista e imprime cada nombre con un saludo, 
# ejemplo: "Hola, Juan!"
# --------------------------------------------
nombres = ["Hector", "Ivan", "Jose", "Juan", "Ana"]

for nombre in nombres:
    print(f"Hola, {nombre}")



# --------------------------------------------
# RETO OPCIONAL (para quien quiera ir más allá)
# Usando list comprehension, crea una lista nueva 
# que contenga solo las temperaturas mayores a 20 grados 
# de tu lista "temperaturas" del Ejercicio 1
# --------------------------------------------
temperaturas = []

tempt1 = float(input("Ingrese la primera temperatura: "))
tempt2 = float(input("Ingrese la segunda temperatura: "))
tempt3 = float(input("Ingrese la tercera temperatura: "))

temperaturas.append(tempt1)
temperaturas.append(tempt2)
temperaturas.append(tempt3)

temperaturas_mayores = [t for t in temperaturas if t > 20]
print (f"las temperaturas mayores son {temperaturas_mayores}")

#EJERCICIOS EXTRA

precios = [800, 1200, 55000, 10000, 24000]
precios_descuento = [p * 0.9 for p in precios ]

print(f"Precio original: {precios}")
print(f"Precio descuento: {precios_descuento}")

# 2

edades = [21, 14, 56, 10, 42, 18]
edad_mayores = []
contador = 0

for edad in edades:
    if edad >= 18:
        edad_mayores.append(edad)
        contador += 1

print(f"Los mayores de edad son: {edad_mayores}")
print(f"En total son {contador} mayores de edad")

# 3

nombres_estudiantes = ["Hector", "Ivan", "Jose", "Juan", "Ana"]
notas_estudiantes = [4.5, 2.2, 5.0, 3.0, 3.5]

for a, b in zip(nombres_estudiantes, notas_estudiantes):
    print(f"La nota del estudiante {a} es {b}")