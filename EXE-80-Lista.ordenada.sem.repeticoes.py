#  Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
#  correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

# if = se
# else = senão
# elif = senão se
# cont = contador
# count = contar
# while = enquanto
# break = parar
# lower = minuscula
# upper = maiuscula
# round = arredondar casas decimais > variavel = round(variavel,2) > C = round(C, 2)
# .sort() > organiza listas de elementos em ordem crescente
# .sort(reverse=True) > ordem decrescente
# len() > retorna o numero de itens em uma variavel
# '{:-^40}.format('texto') > CENTRALIZAR A FRASE
# variavel.index('item') > imprime a posição da variavel
# randint > sorteia valores
# max > maior valor
# min > menor valor
# tuplas usa parentes > lanche = ('baguncinha','suco','pizza','pudim') print(lanche[0])
# listas usa colchetes > lanche = ['baguncinha','suco','pizza','pudim']
# append > inclui um item
# insert > insere um item conforme indicação na lista
# deletar > dellanche[3] / lache.pop(3) ou lance.pop() elimina o ultimo / lache.remove(indicar o valor)
# enumerate > varre a lista

lista = list()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionando na posição {pos} da lista.')
                break
            pos += 1
print(f'Os valores digitados foram {lista}')
