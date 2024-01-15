# TUPLAS EM PYTHON > guardam vários valores > são imutaveis
# no python mais novos a tupla pode ser sem parenteses

lanche = ('baguncinha','suco','pizza','pudim' )
#               0        1       2       3
#              -4       -3      -2      -1
'''
print(lanche[0:3])      #print(lanche[1])   #print(lanche[-2:])

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

for comida in lanche:
    print(f'Eu vou comer {comida}')

# identificando a posição

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')'''

# posição em tuplas
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.index(8))   # quero saber qual é posição do numero 8 na tupla