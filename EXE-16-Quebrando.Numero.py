# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

# bloquear todo o script de execução é so utlizar 3 aspas simples no começo e no final como exemplo abaixo
'''from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua parte inteira é {}'.format(num, math.trunc(num)))'''

#---------------------------------------------------------------------------------------------
# como utilizou apenas um math optou por utilizar from math import
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua parte inteira é {}'.format(num, math.trunc(num)))

'''outra forma abaixo'''

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua parte inteira é {}'.format(num, int(num)))