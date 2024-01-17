#  Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final,
#  mostre uma listagem de preços, organizando os dados em forma tabular.

# if = se
# else = senão
# elif = senão se
# cont = contador
# count = contar
# while = enquanto
# break = parar
# round = arredondar casas decimais > variavel = round(variavel,2) > C = round(C, 2)
# '{:-^40}.format('texto') > CENTRALIZAR A FRASE
# TUPLAS
# variavel.index('item') > imprime a posição da variavel
# randint > sorteia valores
# max > maior valor
# min > menor valor

listagem = ('lapis', 1.75,'borracha', 2,'caderno', 10,'estojo', 1.75,'livros', 1.75,
            'transferido', 1.75,'compasso', 1.75,'mochila', 50,'canetas', 1.75,)
print('_' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')   # centralizado
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')

'''
________________________________________
          LISTAGEM DE PRESÇOS           
lapis.........................R$   1.75
borracha......................R$   2.00
caderno.......................R$  10.00
estojo........................R$   1.75
livros........................R$   1.75
transferido...................R$   1.75
compasso......................R$   1.75
mochila.......................R$  50.00
canetas.......................R$   1.75

'''