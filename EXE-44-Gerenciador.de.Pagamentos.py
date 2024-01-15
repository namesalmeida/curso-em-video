# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
# e condição de pagamento:

print('{:=^40}'.format('  LOJAS NAMIX  '))
preço = float(input('Preço das compras: R$ '))
print('''FORMA DE PAGAMENTO
[ 1 ] à vista DINHEIRO/CHEQUE
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(totparc, parcela))
else:
    total = preço
    print('Opção invalidada de pagamento. Tente novamente')
print('Sua compra de R$ {:.2f} vai custar R${:.2f} no final.'.format(preço, total))
