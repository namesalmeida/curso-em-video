# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
# for = A estrutura de repetição FOR executa um ciclo para cada elemento do objeto que está sendo iterado.

n = int(input('Digite um numero? '))
for d in range(1, 11):
    print('{} x {:2} = {}'.format(n, d, n*d))