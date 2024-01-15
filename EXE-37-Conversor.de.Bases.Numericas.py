# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será
# a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertida para HEXADECIMAL é igual a {}'.format(num, hex(num)))
else:
    print('opção invalida, tente novamente')