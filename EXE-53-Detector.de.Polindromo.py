# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos: Palindromos são palavras escrito invertido e fica a mesma coisa.
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

# strip -> retira os espaços
# upper -> faz tudo ficar maiuscula

frase = str(input('Digite uma frase: ')).strip().upper()    # NAMES ALMEIDA DA SILVA
palavras = frase.split()
print('Você digitou a frase {}'.format(frase))

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

frase = str(input('Digite uma frase: ')).strip().upper()    #['NAMES', 'ALMEIDA', 'DA', 'SILVA']
palavras = frase.split()
print('Você digitou a frase {}'.format(palavras))

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = '*'.join(palavras)     #junta as palavras, retira os espaços > NAMES*ALMEIDA*DA*SILVA
print('Você digitou a frase {}'.format(junto))

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]                     #inverte a frase ou palavra
print(junto, inverso)
if inverso == junto:                            #se inverso for igual a junto
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

# outra forma
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]                           # fatiamento
print(junto, inverso)
if inverso == junto:                            #se inverso for igual a junto
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')