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
47 > cinza

\033[0:30;41m]
\033[4;33;44m]'''

print('-=-' * 20)

print('\033[1;33;44mOlá, Mundo!')                         # [1      ;     33   ;     44m
else:                                                     #  estilo |cor texto | cor de fundo
print('\033[4;31;43mOlá, Mundo!\033[m')                   # \033[m' no final para limitar a cor de fundo

print('-=-' * 20)

a = 35632478
b = 4
print('Os valores são \033[33;31m{}\033[m e \033[35m{}\033[m!!!'.format(a, b))

print('-=-' * 20)
print('Outra forma')
nome = 'Names'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

print('-=-' * 20)
print('Outra forma')
nome = str(input('Digite seu nome: '))
cores = {'limpa':'\033[m',
         'azul':'\033[4;34m',
         'amarelo':'\033[4;33m',
         'pretoebranco':'\033[4;30;40m'}

print('Olá! muito prazer em te conhecer, {}{}{}'.format(cores['azul'], nome, cores['limpa']))
print('Olá! muito prazer em te conhecer, {}{}{}'.format(cores['amarelo'], nome, cores['limpa']))
print('Olá! muito prazer em te conhecer, {}{}{}'.format(cores['pretoebranco'], nome, cores['limpa']))