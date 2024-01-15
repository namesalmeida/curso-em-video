# Nessa aula, vamos continuar a estudar os laços e vamos aprender a usar a
# estrutura de repetição while no Python. Por exemplo:

# Operadores relacionais
# == igual a
# != diferente
# >= maior ou igual
# > maior que
# < menor que
# <= Menor ou igual

# > while = enquanto

c = 1
while c !=10:   # condição de parada é 10
    print(c)
    c+=1        # c = c + 1 é o mesmo que c += 1
print('Acabou')
'''
#----------------------------------------------------------------------------------------

r = 'S'
while r == 'S':     # Enquanto digitar SIM 'S' ele vai continuar perguntando um valor
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')
'''
#----------------------------------------------------------------------------------------

n = 1
par = impar = 0                         # quando digitar 0 ele para.
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:                          # (!=) significa diferente
        if n% 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} numeros pares e {} números ímpares!'.format(par, impar))