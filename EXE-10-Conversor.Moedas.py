# 1 > incluir o valor do dolar e euro hoje
n = float(input('Quanto dinheiro voce tem na carteira? R$ '))
d = float(input('Qual é a cotação do dolar hoje? R$ '))
e = float(input('Qual é a cotação do euro hoje: R$ '))
d1 = n / d
e1 = n / e
print('Com R${:.2f} você pode comprar ${:.2f} dolares ou ${:.2f} euros'.format(n, d1, e1))

# 2 > fixa o favor do dola na sintaxe
n = float(input('Quanto dinheiro voce tem na carteira? R$ '))
d = n / 4.85
print('Com R${:.2f} você ponde comprar ${:.2f}'.format(n, d))