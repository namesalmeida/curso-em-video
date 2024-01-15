# As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura,
# acessíveis por chaves individuais. As litas são mutaveis, podem ser modificadas.

# tuplas usa parentes > lanche = ('baguncinha','suco','pizza','pudim') print(lanche[0])
# listas usa colchetes > lanche = ['baguncinha','suco','pizza','pudim']
# append > inclui um item
# insert > insere um item conforme indicação na lista
# deletar > dellanche[3] / lache.pop(3) ou lance.pop() elimina o ultimo / lache.remove(indicar o valor)

num = [4, 5, 9, 1]
#num[4] = 7
num.append(7)                       # > [4, 5, 9, 1, 7]
num.sort(reverse=True)              # > [9, 7, 6, 5, 4, 1]
num.insert(2, 6)   # > [4, 5, 6, 9, 1, 7]
#num.pop(1)
num.remove(4)
print(num)
print(f'Essa lista tem {len(num)}') # > lê a quantidade de elementos

# -------------------------------------------------------------------------------------------

valores = list()
for cont in range (0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na poisição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')


A = [4, 5, 4, 1]
B = A[:]                            # receber uma copia de A
B[2] = 8                            # Lista B: [4, 5, 8, 1]
print(f'Lista A: {A}')
print(f'Lista B: {B}')