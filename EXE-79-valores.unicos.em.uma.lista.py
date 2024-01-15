#  Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número
#  já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

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

numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
#    elif != 'SsNn':
#       print('opção incorreta digite novamente!')
numeros.sort()
print(f'Você digitou os valores {numeros}')