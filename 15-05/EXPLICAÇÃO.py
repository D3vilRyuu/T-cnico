# index - (indice) retorna o indice de um elemento em uma lista.
# EX:

vegetais = ['Tomate','Alface', 'Brocolis']

print( vegetais.index('Alface'))
posicaoTomate = vegetais.index('Alface')

# count - (Contar) retorna a quantidade de ocorrências de um elemento na lista.
# EX:
vegetais.append('Tomate')
print(vegetais)
print( vegetais.count('Tomate') )

# sort - Ordena de forma crescente os elementos de uma lista, desde que esses elementos sejam ordenaveis.
# EX:

vegetais.sort()
print(vegetais)

# reverse - Ordena de forma descrecente os elementos da lista, desde que os elementos da lista sejam ordenaveis.
# EX:

vegetais.reverse()
print(vegetais)

