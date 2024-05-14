# 4 - Crie uma lista de idades com várias idades diferentes e retorne uma segunda lista, 
# com todas as idades acima de 18 anos. 

idades_tot = [16,18,22,15,10,28]
maior = 18
idades_maior = []

for idade in idades_tot:
    if idade > maior:
        idades_maior.append(idade)
    
print(idades_maior)
