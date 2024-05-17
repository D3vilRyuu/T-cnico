# 1 - Crie um programa que armazene uma lista de notas e ordene as mesmas em nota crescente. Em seguida, 
# o programa deve exibir todas as notas maiores ou iguais a 5.

notas = [5,4,7,8,10]
maior = 5
notas.sort()
notas_acima = []

for i in notas:
    if i >= maior:
        notas_acima.append(i)

print(f"Todas as notas: {notas}")
print(f"Notas igual ou acima de 5: {notas_acima}")