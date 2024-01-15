# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
# > for = A estrutura de repetição FOR executa um ciclo para cada elemento do objeto que está sendo iterado.
from time import sleep
for cont in range(0, 11):   # de 0 a 10 > se colocar 1 no lugar de 0 vai de 1 a 10
    print(cont)
    sleep(1)
print('FELIZ ANO NOVO')

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

for cont in range(10, -1, -1):  # vai de 10 a 1
    print(cont)
    sleep(1)
print('FELIZ ANO NOVO')