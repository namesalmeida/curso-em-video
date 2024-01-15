# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do
# grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaidade = 0               #|
mediaidade = 0              #|
maioridadehomem = 0         #  > Variáveis
nomevelho = 0               #|
totmulher20 = 0             #|
for p in range(1, 5):
    print('------- {} PESSOA ------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':                 # Mm maisculo e minusculo por conta da variavel Sexo, o usuario pode digitar das 2 formas
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:             # Ff miusculo e minusculo por conta da variavel Sexo, o usuario pode digitar das 2 formas
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))