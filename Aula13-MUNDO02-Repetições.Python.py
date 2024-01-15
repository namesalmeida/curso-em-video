# laço de repetição ou iteração
# for = A estrutura de repetição FOR executa um ciclo para cada elemento do objeto que está sendo iterado.
#for c rang(...
'''for c in range(0, 6):    #irá replicar 6x
    print('oi')'''

for c in range(0, 7):   # ira contar de 0 a 6
    print(c)
print('FIM')

for c in range(6, 0, -1):   # ira contar de tras para frente de 6 a 1
    print(c)
print('FIM')

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

for c in range(0, 4):   # irá pedir valores 4x
    n = int(input('Digite um valor: '))
print('fim')

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

s = 0
for c in range(0, 4):   # irá pedir valores 4x e somar
    n = int(input('Digite um valor: '))
    s = s + n
    # s += n
print('A soma dos valore é {}'.format(s))