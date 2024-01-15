# Interrompendo Repetições While com Brake
# ao inves de digitar .format > incluir a string antes da aspas simples > print(f'A soma vale {s}')
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')
