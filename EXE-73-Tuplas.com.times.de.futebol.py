# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

# if = se
# else = senão
# elif = senão se
# cont = contador
# while = enquanto
# break = parar
# round = arredondar casas decimais > variavel = round(variavel,2) > C = round(C, 2)
# '{:-^40}.format('texto') > CENTRALIZAR A FRASE
# TUPLAS
# variavel.index('item') > imprime a posição da variavel

times = ('Bragantino', 'Athletico-PR', 'Fortaleza', 'Palmeiras', 'Atlético-GO',
         'Atlético-MG', 'Flamengo', 'Fluminense', 'Bahia', 'Santos', 'Cotinthians',
         'Ceará SC', 'Internacional','Juventude', 'Sport Recife', 'Cuiabá',
         'Chapecoense', 'São Paulo', 'América-MG', 'Grêmio')

print(f'lista de times: {times}')
print('*-' * 20)
print('a) Os 5 primeiros times.')
print(times[0:5])
print('*-' * 20)
print('b) Os últimos 4 colocados.')
print(times[-4:])
print('*-' * 20)
print('c) Times em ordem alfabética.')
print(f'Times em ordem alfabética: {sorted(times)}')
print('*-' * 20)
print(f'O Chapecoense está na posição {times.index("Chapecoense")+1}')

### print embaixo um do outro
for t in times:
    print(t)

nasc = int(input('Qual é o seu ano de nascimento? '))
atual = int(input('Digite o ano atual: '))
idade = atual - nasc
print(f'Sua idade atual é {idade} anos')

