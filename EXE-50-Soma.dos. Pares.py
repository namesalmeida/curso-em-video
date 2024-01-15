# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

# for = A estrutura de repetição FOR executa um ciclo para cada elemento do objeto que está sendo iterado.

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:                        #para achar numero par o resultado da divisão tem que dar 0
        soma = soma + num
        cont = cont + 1
print('Você informou {} números pares e a soma foi {}.'.format(cont, soma))