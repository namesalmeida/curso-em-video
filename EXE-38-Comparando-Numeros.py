n1 = int(input('primeiro numero: '))
n2 = int(input('segunto numero: '))
if n1 > n2:
    print('O primeiro valor é maior')
elif n2 > n1:
    print('O segundo valor é maior')
else:                                   #não há necessidade de incluir == pois não ha outra opção nesta situação.
    print('Os números são iguais')
