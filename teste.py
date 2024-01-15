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
'''
nasc = int(input('Qual é o seu ano de nascimento? '))
atual = int(input('Digite o ano atual: '))
idade = atual - nasc
print(f'Sua idade atual é {idade} anos')

F = float(input('Qual é a temperatura nos USA: '))
C = (F - 32) / 1.8
C = round(C, 2)
print(f'Convertido para Celsius fica {C}º ')'''

N1 = float(input('Primeira nota: '))
N2 = float(input('Segunda nota: '))
M = (N1 + N2) / 2
if M >= 7:
    print(f'Você esta aprovado, Sua média foi {M}.')
elif M < 7:
    print(f'Você esta reprovado, Sua média foi {M}.')

C = (F - 32) / 1.8
F = float(input('Qual é a temperatura nos USA: '))
C = round(C, 2)
print(f'Convertido para Celsius fica {C}º ')