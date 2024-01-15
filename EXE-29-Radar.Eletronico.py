# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem
# dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
# o exemplo abaixo é uma condição simples pois utiliza somente o if

velocidade = float(input('Qual é a velocidade do carro? '))
if velocidade > 80:
    print('INFRAÇÃO! Voce excedeu o limite permitido que é de 80 km/h')
    multa = (velocidade - 80) * 7
    print('Voce irá pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
