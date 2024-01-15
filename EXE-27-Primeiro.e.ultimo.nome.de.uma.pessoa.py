'''Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando
em seguida o primeiro e o último nome separadamente'''
# split() > fatia o nome = 'Names','Almeida','da,'Silva'
# [len(nome)-1] > vai me dizer quantas posições tem o nome |
# o -1 é para que nao leia o 0 (zero) pq em python considera o 0(zero) na contagem
# por exemplo se nao tiver -1 o almeida irá aparecer na posição 1

n = str(input('Digite seu nome: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)]))
