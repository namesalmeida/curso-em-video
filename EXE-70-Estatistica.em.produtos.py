# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
# continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

# if = se
# else = senão
# elif = senão se
# cont = contador
# while = enquanto
# break = parar
# '{:-^40}.format('texto' > CENTRALIZAR A FRASE

print('-#-#' * 10)
print('{:-^40}'.format('N-MIX INFORMATICA'))        # '{:-^40} > CENTRALIZAR A FRASE
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi de R$ {total:.2f}')
print(f'Temos {totmil} produto(s) custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')