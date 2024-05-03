# Escreva um programa que leia do usuário o comprimento dos três lados de um triângulo, e partir dessas
# informações verifique se este triângulo é:

# A)Equilatero
# B)Isoceles
# C)Escaleno

lado1 = float(input("Comprimento do primeiro lado do triângulo: "))
lado2 = float(input("Comprimento do segundo lado do triângulo: "))
lado3 = float(input("Comprimento do terceiro lado do triângulo: "))

if lado1 == lado2 == lado3:
    print("É um triângulo é equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("É um triângulo é isósceles.")
else:
    print("É um triângulo é escaleno.")