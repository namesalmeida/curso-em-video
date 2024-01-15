#'Curso em vido Python' > cadeia de caracteres
#[] > itens em colchetes é lista
# toda string começa com o numero 0

'''FATIAMENTO'''
#curso em video p y t h o n
#01234567891011121314151617181920
''' frase[9:13] video   > sempre colocar uma casa a mais [9:14]
    frase[9:21:2]       > vai do 9 até o 21 saltando de 2 em 2
    frase[:5]           > vai começar do 0 e vai até 5
    frase[15:]          > vai do 15 até o final
    frase[9::3]         > vai do 9 até o final saltando de 3 em 3
    frase = 'Curso em Video Python'
#----------------------------------------------------#----------------------------------------------------

'''Analise do string
#len > comprimento da frase
frase = 'Curso em Video Python'
len(frase)
Resultado: len = 21 caracteres
print(len(frase))
print(len(frase.strip()))

#----------------------------------------------------#----------------------------------------------------
#count > contar quantas vezes um caracter esta na frase
frase.count('o') > vai contar quantas vezes a letra aparece na frase
Resultado: frase = 3
> frase.count('o',0,13) > entre o caracter zero (0) e o treze (13) tem apenas uma letra 0


#----------------------------------------------------#----------------------------------------------------
#find > encontrar
> frase.find('deo') > vai mostrar a posição que a frase esta
resultado = posição de 11 a 13

#----------------------------------------------------#----------------------------------------------------
# operador 'in' > irá dizer se a palavra esta na frase, se tiver irá aparecer TRUE

#----------------------------------------------------#----------------------------------------------------
# replace > trocar/substituir
frase.replace('Python','Android') > onde estiver python irá substituir por android

#----------------------------------------------------#----------------------------------------------------
# upper > transforma em maiusculas 'UPPER'
frase.upper()
print(frase.upper(''))

#----------------------------------------------------#----------------------------------------------------
# lower > transforma em minusculas 'lower'
frase.lower('')
print(frase.lower().find('video'))

#----------------------------------------------------#----------------------------------------------------
# capitalize > transforma em minuscula somente a primeira letra fica em maiuscula
frase.capitalize('')

#----------------------------------------------------#----------------------------------------------------
# title > transforma em maiuscula somente a primeira letra das palavras da frase
print(frase.title(''))

#----------------------------------------------------#----------------------------------------------------
# strip > remove os espaços a mais
frase.strip()
print(frase.strip(''))

#----------------------------------------------------#----------------------------------------------------
# rstrip > remove os espaços a mais da direita e mantem da esquerda
frase.strip()
print(frase.rstrip(''))

#----------------------------------------------------#----------------------------------------------------
# lstrip > remove os espaços a mais da esquerda e mantem da direita
print(frase.lstrip(''))

#----------------------------------------------------#----------------------------------------------------
#funcionalidades de Divisão
split > vai dividir em lista todas as palavras de uma cadeia de caracteres
frase = 'Curso em Video python'
print(frase.split()) > resultado ['Curso', 'em', 'Video', 'python']

frase = 'Curso em Video python' > separa as palavras, separado pelo seu splitador
'curso','em','video','python'
dividido = frase.split()
print(dividido[2][3]) > Resultado = e

#----------------------------------------------------#----------------------------------------------------
#Em textos grandes utilizar print("""texto grande""")

#----------------------------------------------------#----------------------------------------------------
'-'.join(frase) > vai juntar a frase

