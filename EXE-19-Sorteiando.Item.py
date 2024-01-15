# random — Gerar números pseudo-aleatórios
# choice() é uma função embutida na linguagem de programação Python que retorna um item aleatório de uma lista
# random.choice retorna um elemento da sequência sorteada

import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto Aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

#----------------------------------------------------

from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto Aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
