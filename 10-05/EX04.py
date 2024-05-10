# 4 -Crie um programa que receba uma lista de números e retorne qual o maior elemento da lista.
import math
numeros = [0,2,6,4]
maior = -2147483648

for i in numeros:
    if(i > maior):
        maior = i

print(maior)

# print(max(numeros)) outro modo de se retirar o maior elemento
    
