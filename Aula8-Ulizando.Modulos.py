# bibliotecas > ex. Bebidas: agua, suco, refrigerante, vinho etc.
# bibliotecas > ex. comida: pizza, cachorro quente, caldo

#comandos


# bliblioteca MATH  > import math | > from('math')import('sqrt')
    # ceil > arredonta para cima > ex.: math.ceil(raiz)
    # floor > arredonta para baixo > ex.: math.floor(raiz)
    # trunc > vai truncar, eliminar numeros depois da virgula
    # pow > potencia funciona igual a **
    # sqrt > calcular raiz quadrada
    # factorial > calcular fatoração'''

# import math > importa de forma geral ou seja importa tudo que esta dentro da biblioteca
# from math import sqrt > este comando importa algo especifico dentro da biblioteca neste caso sqrt

#------------------------------------------------------------------------------------

import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))

# outra forma

import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

#-------------------------------------------------------------------------------------

# utilzando comandos com FROM

from math import sqrt, floor
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))

