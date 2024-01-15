# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um numero: '))
resultado = num % 2                             #todo numero impar o resto da divisão é 1, todo par o resto é 0
#print('O resultado foi {}'.format(resultado))
if resultado == 0:
    print('O numero {} é PAR'.format(num))
else:
    print('O numero {} é IMPAR'.format(num))