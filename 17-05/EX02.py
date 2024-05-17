# 2 - Crie um programa que armazene uma lista de nomes e permita que o usuário busque uma nome específico na 
# lista. Se o nome existir, o programa deve retornar o indice do nome procurado, se não, deve retornar 
# "Nome não encontrado"

nomes = ["Pedro","Ramon","Thiago","Joao"]
nome_usu = input("Digite um nome que deseja buscar: ")

for i in nomes:
    if nome_usu == i: 
        indice = nomes.index(i)
        print(f"Nome: {i}, Sua posição é: {indice}")
    else:
        print("Nome não encontrado!")

