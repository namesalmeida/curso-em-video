#  Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
#  para cada palavra, quais são as suas vogais.

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
# TUPLAS
# variavel.index('item') > imprime a posição da variavel
# randint > sorteia valores
# max > maior valor
# min > menor valor

palavras = ('names', 'cadeira', 'linha', 'computador', 'celular', 'mouse', 'grátis')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aàáâãeéiíoõôóuúù':
            print(letra, end=' ')   # com o espaço dentro da aspas simples fica separado as letras
