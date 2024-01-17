#Crie um programa que vai ler vários números e colocar em uma lista.
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

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

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('*-' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor de 5 esta na lista.')
else:
    print('O valor de 5 não se encontra na lista.')
