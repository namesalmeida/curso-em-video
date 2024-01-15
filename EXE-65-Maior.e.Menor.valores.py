# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores.

# if = se
# else = senão
# elif = senão se
# cont = contador
# while = enquanto
# break = parar

soma = 0
quant = 0
media = 0
maior = 0
menor = 0
resp = 'S'
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip() [0]
media = soma / quant
print('Você digitou {} números, e a média foi de {}.'.format(quant, media))
print('O maior valor foi  {} e o menor foi {}.'.format(maior, menor))
