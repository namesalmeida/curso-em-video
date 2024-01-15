#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

peso = float(input('Qual é o seu peso atual? (kg) '))
altura = float(input('Qual é a sua altura? (m) '))
IMC = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1F}'.format(IMC))
if IMC < 18.5:
    print('Você esta ABAIXO DO PESO normal')
elif 18.5 <= IMC < 25:
    print('Parabens, voce esta na faixa normal')
elif 25 <= IMC < 30:
    print('Você esta em SOBREPESO')
elif 30 <= IMC < 40:
    print('Você esta com Obesidade')
#else:
elif IMC >= 40:
    print('Cuidado você esta com Obesidade Morbida')