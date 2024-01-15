#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o
# jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

# Na lista de unicodes, substitua “+” por “000”. Por exemplo – “U+1F600” se tornará
# “U0001F600” e prefixe o unicode com “\” e imprima-o.
# lista de emojis: https://unicode.org/emoji/charts/full-emoji-list.html#1f928

# \n causa quebra de linha

import emoji
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador <= computador:
            print('Mais... Tente mais uma vez.\U0001FAE3')
        elif jogador > computador:
            print('Menos... Tente mais uam vez.\U0001F606')
print('Acertou miseravi \U0001F923 com {} tentativas. \nParabéns!'.format(palpites))    # \n causa quebra de linha
# para incluir emogi é so incluir \U0001f600 barra com o codigo do emogi.
if palpites < 5:
    print('\U0001F44F')
elif palpites > 5:
    print('\U0001F62C')
