# 2 - Escreva um programa que receba uma lista e conte quantos elementos ela possui, e retorne esse valor. 
nomes = ["Thiago","Ramon","Pedro","Davi"]
elementos = 0

for quant_elem in nomes:
    print(quant_elem)
    elementos += 1 

print(f"A quantidade de elementos é de {elementos}")

# print(len(nomes)) outra forma de contar elementos
