'''Escreva um programa que solicite ao usuário a entrada de um número
inteiro positivo ou negativo e mostre a quantidade de dígitos desse
número.'''
numero = input("Digite um inteiro positivo ou negativo:")
digitos = '0123456789'
cont = 0
if numero[0] == '-' or numero[0] == '+':
    i = 1
    while i<len(numero):
        if numero[i] in digitos:
            cont+=1
        i+=1
elif numero[0] in digitos:
    i = 0
    while i<len(numero):
        if numero[i] in digitos:
            cont+=1
        i+=1
print(f"Total de dígitos: {cont}")