# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''upper > para ficar tudo maiuscula
   frase.find('A')+1)) > para saltar o 0 na contagem da posição, pois no python a contagem começa do zero 0
   frase.rfind('A')+1)) > o r de rfind quer dizer que procure a partir do lado direito | find = encontrar
   strip() > retira os espaços a mais quando o usuario digita errado'''

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparecer {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))