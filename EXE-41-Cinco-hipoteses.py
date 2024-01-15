# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
# sua categoria, de acordo com a idade:

from datetime import date # pegar ano atual
atual = date.today().year # puxa o ano atual
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('O atleta tem {}'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <=25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')