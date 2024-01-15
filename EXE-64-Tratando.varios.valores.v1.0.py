# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre
# eles (desconsiderando o flag).

n = 0       #\
cont = 0    # >>>> n = cont = soma = 0
soma = 0    #/
n = int(input('Digite um numero [999 para parar]: '))
while n != 999:
    soma += n       # é a soma dos numeros
    cont += 1
    n = int(input('Digite um numero [999 para parar]: '))
print(f'Você Digitou {cont} numeros. E a soma deles foi {soma}.')

