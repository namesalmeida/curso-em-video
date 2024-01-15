'''Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.'''
# operador > in
# LOWER > MINUSCULO
# UPPER > MAIUSCULO

nome = str(input('Digite seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))

nome = str(input('Digite seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.upper()))