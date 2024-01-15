c = float(input('Qual é o valor do imóvel? '))
s = float(input('Qual é o seu salário? '))
anos = int(input('Em quantos anos deseja pagar? '))
prest = c / (anos * 12)
minimo = s * 30 / 100
print('Para pagar uma casa de R${:.2f} anos'.format(c, anos), end=' ') # ,end=' ') linha de baixo continuar
print('a prestação será de R${:.2f}'.format(prest))
if prest <= minimo:
    print('EmprÉstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO por que o valor da parcela é maior que 30% do seu salário')