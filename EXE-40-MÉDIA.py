# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:

n1 = float(input('Primeira nota? '))
n2 = float(input('Segunda nota? '))
media = (n1 + n2) / 2
print('Sua média é {}'.format(media))
if media < 5.0:
    print('Você esta reprovado, sua média {} é menor que a média 5.0'.format(media))
elif media >= 5.0:
    print('Você esta aprovado, sua média de {} é maior/igual a 5.0'.format(media))
