# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

temp = list()
princ = list()
mai = men = 0
while True:
    temp.append(str(input('Digite um nome: ')))
    temp.append(float(input('Digite o peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])                           #cria uma copia fatiada de temp
    temp.clear()                                    # irá limpar o temp para não duplicar valores
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'Os dados foram {princ}')
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')  #len faz leitura da quantidade.
print(f'O maior peso foi de {mai}kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]}')
print(f'O menor peso foi de {men} kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'{p[0]}', end='')
