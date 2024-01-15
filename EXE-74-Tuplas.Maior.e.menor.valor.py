# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
# números gerados e também indique o menor e o maior valor que estão na tupla.

# if = se
# else = senão
# elif = senão se
# cont = contador
# while = enquanto
# break = parar
# round = arredondar casas decimais > variavel = round(variavel,2) > C = round(C, 2)
# '{:-^40}.format('texto') > CENTRALIZAR A FRASE
# TUPLAS
# variavel.index('item') > imprime a posição da variavel
# randint > sorteia valores
# max > maior valor
# min > menor valor

from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10),
    randint(1,10), randint(1,10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')