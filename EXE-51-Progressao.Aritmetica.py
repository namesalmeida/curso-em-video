# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão

# for = A estrutura de repetição FOR executa um ciclo para cada elemento do objeto
# que está sendo iterado.

n1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = n1 + (10 - 1) * razao
for c in range(n1, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('Acabou')