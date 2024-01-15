# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
if a<b and a>c:
    menor = a
if b<c and b<a:
    menor = b
if c<a and c<b:
    menor = c
print('O menor valor digitado é {}'.formart(menor))

# -----------------------------------------------------------------------------
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Teceiro valor: '))
#Verificar menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificar maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado é {}'.format(maior))
print('O menor valor digitado é {}'.format(menor))