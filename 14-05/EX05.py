# 5 - Crie um programa com uma lista com diversos números e que a partir dela, gere duas novas listas, 
# uma com todos os números pares contidos na primeira lista, e outra com todos os números ímpares.

numeros = [2,7,3,4,23,87,21,23,76,34,5]
numeros_pares = []
numeros_impares = []

for n in numeros:
    if n % 2 == 0:
        numeros_pares.append(n)
    else:
        numeros_impares.append(n)

print(numeros)
print(numeros_pares)
print(numeros_impares)
