# if = se
# else = senão
# elif = senão se
# cont = contador
# while = enquanto
# break = parar

'''O elif posso utilizar quantas vezes forem necessarias, já o else apenas uma vez'''

nome = str(input('Qual é o seu nome: '))
if nome == 'Names':
    print('Que nome bonito')
elif nome =='Karyn' or nome == 'Karine' or nome == 'Smilinguido':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Omoacy Marilheuza Moniza Andre':
    print('Belo nome')
else:
    print('Seu nome é bem normal.' )
print('Tenha um um bom dia, {}!'.format(nome))

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
