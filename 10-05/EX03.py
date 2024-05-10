# 3 - Crie um programa que receba uma lista de números e calcule a média dos elementos.

numeros = [0,2,4,6]
soma = 0
elementos = 0

for somar in numeros:
    soma += somar
    elementos += 1

media = soma / elementos
print (media)

