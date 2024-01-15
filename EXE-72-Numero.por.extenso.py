# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

# if = se
# else = senão
# elif = senão se
# cont = contador
# while = enquanto
# break = parar
# '{:-^40}.format('texto') > CENTRALIZAR A FRASE
# TUPLAS

ext = ('zero','um','dois','três','quatro',
        'cinco','seis','sete','oito','nove',
        'dez','onze','doze','treze',
        'quatorze','quinze','dezesseis',
        'dezessete','dezoito','dezenove','vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {ext[num]}')