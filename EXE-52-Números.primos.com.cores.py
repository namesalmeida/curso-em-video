# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# for = A estrutura de repetição FOR executa um ciclo para cada elemento do objeto que está sendo iterado.

''' style: 0 / 1 / 4 / 7
0 > nada > sem estilo
1 > bold > negrito
4 > sublinhado
7 > inverter

text cores
30 > branco
31 > vermelho
32 > verde
33 > amerelo
34 > azul
35 > magenta
36 > ciano
37 > cinza

back > corres de fundo
40 > branco
41 > vermelho
42 > verde
43 > amarelo
44 > azul
45 > roxo
46 > cyan
47 > cinza'''

p = int(input('Digite um numero: '))
tot = 0
for c in range(1, p + 1):
    if p % c == 0:
        print('\033[33m', end='')       # [33m é a cor (ver no cores no python.py)
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[1;31;40m O numero {} foi divisivel {} vezes\033[m'.format(p, tot))
if tot == 2:
    print('\n\033[1;34;40m E por isso ele é PRIMO\033[m')       # [1      ;     35   ;     40m
else:                                                           #  estilo |cor texto | cor de fundo
    print('\n\033[1;31;40m Por isso ele não é PRIMO\033[m')