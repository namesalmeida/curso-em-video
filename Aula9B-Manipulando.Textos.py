frase = 'Curso em Video python'
print(frase[3:13])                  #vai busar da posição 3 até a 13 na frase
print(frase[::2])                   #vai buscar na frase inteira saltando de dois em dois > Croe ie yhn
print(frase.count('p'))             #vai contar quantas letras 'p' tem na frase
print(frase.upper())                #vai alterar todas as palavras para maiuscula
print(frase.upper().count('O'))     #vai colocar o texto em maiuscula e contar quantas letros 'O' maiuscula tem no texto
print(len(frase))                   #ver qual é tamanho da frase
print(len(farse.strip()))           #ver o tamanho da frase e nao conta espaços vazios
print(frase.lower().find('video'))  #faz a busca da palavra em minuscula transformada por lower em minuscula

print(frase.split())                #divide a frase em palavras 'Curso','Video','python'
frase = 'Curso em Video python'
dividido = frase.split()            #irá dividir a frase em palavras
print(dividido[3])                  #vai apresentar a palavras que estão na posição 2 'Video'


#> Para que o Replace funcione deve-se receber o replace dentro do objeto que esta sendo substituido no caso abaixo
#> frase =recebe frase.replace | uma instring é imutavel, unica forma é fazer uma função (REPLACE) e faça uma atribuição
frase = 'Curso em video python'
frase = frase.replace('python', 'android')
print(frase)'''

# texto grande > print("""textotextotextotextotextotextotextotextotextotextotextotextotextotextotexto""")