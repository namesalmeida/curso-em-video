preco = float(input('Qual é preço do produto? R$ '))
percent = float(input('Percentual de desconto? '))
novo = preco - (preco * percent / 100)
print('Na promoção com desconto de {}%, o valor do produto é de R$ {:.2f}'.format(percent, novo))