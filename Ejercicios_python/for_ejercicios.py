# ============================================
# GUÍA Y EJERCICIOS - For y List Comprehension
# ============================================

# --------------------------------------------
# RECORDATORIO: ¿QUÉ ES UN FOR?
# --------------------------------------------
frutas = ["manzana", "pera", "uva"]
for fruta in frutas:
    print(fruta)

numeros = [10, 20, 30]
total = 0
for numero in numeros:
    total = total + numero
print(total)


# ============================================
# NIVEL BÁSICO
# ============================================

# Ejercicio 1
colores = ["rojo", "azul", "verde", "amarillo"]
for color in colores:
    print(f"Color: {color}")

# Ejercicio 2
precios = [15000, 22000, 8000, 35000]
total_precios = 0
for precio in precios:
    total_precios = total_precios + precio
print(total_precios)

# Ejercicio 3
edades = [15, 22, 17, 30, 12, 19]
contador_mayores = 0
for edad in edades:
    if edad >= 18:
        contador_mayores = contador_mayores + 1
print(contador_mayores)

# Ejercicio 4
notas = [3.5, 4.2, 2.8, 4.8, 3.9]
nota_mas_alta = notas[0]
for nota in notas:
    if nota > nota_mas_alta:
        nota_mas_alta = nota
print(nota_mas_alta)

# Ejercicio 5
numeros_base = [1, 2, 3, 4, 5]
dobles = []
for numero in numeros_base:
    dobles.append(numero * 2)
print(dobles)


# ============================================
# NIVEL INTERMEDIO
# ============================================

# Ejercicio 6
frutas_repetidas = ["manzana", "pera", "manzana", "uva", "manzana"]
contador_manzana = 0
for fruta in frutas_repetidas:
    if fruta == "manzana":
        contador_manzana = contador_manzana + 1
print(contador_manzana)

# Ejercicio 7
numeros_mixtos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
impares = []
for numero in numeros_mixtos:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(pares)
print(impares)

# Ejercicio 8
orden_original = ["a", "b", "c", "d", "e"]
invertida = []
for elemento in orden_original:
    invertida.insert(0, elemento)
print(invertida)

# Ejercicio 9
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
combinada = []
for elemento in lista_a:
    combinada.append(elemento)
for elemento in lista_b:
    combinada.append(elemento)
print(combinada)


# ============================================
# NIVEL AVANZADO / RETO
# ============================================

# Ejercicio 10
con_duplicados = [1, 2, 3, 2, 4, 5, 1, 6]
repetidos = []
for numero in con_duplicados:
    if con_duplicados.count(numero) > 1 and numero not in repetidos:
        repetidos.append(numero)
print(repetidos)


# --------------------------------------------
# LIST COMPREHENSION
# --------------------------------------------
numeros = [1, 2, 3, 4, 5]
cuadrados_largo = []
for n in numeros:
    cuadrados_largo.append(n**2)
cuadrados_corto = [n**2 for n in numeros]
print(cuadrados_largo)
print(cuadrados_corto)

# Ejercicio 11
mixtos = [-5, 3, -2, 8, -1, 10, 0]
positivos = [numero for numero in mixtos if numero > 0]
print(positivos)

# Ejercicio 12 (reto)
numeros_variados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
triples_pares = [numero * 3 for numero in numeros_variados if numero % 2 == 0]
print(triples_pares)