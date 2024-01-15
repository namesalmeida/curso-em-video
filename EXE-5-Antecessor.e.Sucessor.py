n1 = int(input('Digite um numero: '))
a = n1 - 1
s = n1 + 1
print('Analisando o valor {}, Seu antecessor é {}, e seu sucessor é {}'.format(n1, a, s))

#outra forma de fazer abaixo

n2 = int(input('Digite um numero: '))
print('Analisando o valor {}, Seu antecessor é {}, e seu sucessor é {}'.format(n2, (n2-1), (n2+1)))