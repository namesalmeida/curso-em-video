#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever
# na tela se o usuário venceu ou perdeu.

from random import randint                        # random > gerar num aleatorios a partir de uma sequencia determinada
from time import sleep                            # tabela time / metodo sleep > faz esperar por alguns segundos
computador = randint(0, 5)                  # faz o computador "pensar" ou "sortear" randint > inteiros
print('-=-' * 20)                                 # separa as linhas na execuçao -=-=-=-=-=-=-=-=-=-=-
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? ')) # jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)                                          # tempo de espera > neste caso 2 segundos
if jogador == computador:                         # if = se
    print('PARABENS! Voce conseguiu me vencer')
else:                                             # else = então
    print('Você Perdeu, Eu Ganhei! Eu pensei no numero {} e não no {}!'.format(computador, jogador))