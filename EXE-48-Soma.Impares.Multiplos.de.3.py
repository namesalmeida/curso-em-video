# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.
# > for = A estrutura de repetição FOR executa um ciclo para cada elemento do objeto que está sendo iterado.
soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:              #neste caso são os numeros impares divisiveis por 3, ao dividir o resultado é 0.
        cont = cont + 1
        soma = soma + n
print('A soma de todos os {} valores  é {}.'.format(cont, soma))

soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:              #neste caso são os numeros impares divisiveis por 3, ao dividir o resultado é 0.
        cont += 1
        soma += n
print('A soma de todos os {} valores  é {}.'.format(cont, soma))
