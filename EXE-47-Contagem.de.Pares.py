# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
# > for = A estrutura de repetição FOR executa um ciclo para cada elemento do objeto que está sendo iterado.
for n in range(1, 51):
    if n % 2 == 0:              #todo numero impar o resto da divisão é 1, todo par o resto é 0
        print(n, end=' ')
print('Acabou')

# mesma coisa de cima, porém resumido
for n in range(2, 51, 2):
    print(n, end=' ')
print('Acabou')