n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}. \n A raiz quadrada de {} é igual a {:.2f}'.format(n, t, n, r))

# outra forma abaixo

n = int(input('Digite um numero: '))
print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O triplo de {} vale {}. \n A raiz quadrada de {} é igual a {:.2f}'.format(n, (n*3), n, (n**(1/2))))

# outra forma abaixo

n = int(input('Digite um numero: '))
print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O triplo de {} vale {}. \n A raiz quadrada de {} é igual a {:.2f}'.format(n, (n*3), n, pow(n,(1/2))))