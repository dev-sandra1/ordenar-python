
numeros = [1, 5, 8, 12, 3, 7, 10]

valor = 5

# Contar elementos mayores que el valor
conteo = sum(1 for x in numeros if x > valor)

print("Número de elementos mayores que", valor, ":", conteo)
