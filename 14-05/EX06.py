# 6 - Crie um programa com uma lista com várias notas de um aluno,  e calcule a média de todas as notas 
# contidas na lista. 

todas_notas = [7, 6, 9, 5, 4]
soma = 0
elementos = 0

for somar in todas_notas:
    soma += somar
    elementos += 1

media = soma / elementos
print (f"Sua média foi {media}")