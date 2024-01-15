#  Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o
#  menor valor digitado e as suas respectivas posições na lista.

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

valores = []
maior = 0
menor = 0
for c in range (0, 5):                           # lembrando que o 5 será descartado
    valores.append(int(input(f'Digite um valor para a Posição {c}: ')))     # o {c} vai ler a posição
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('*-' * 30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')
print()
