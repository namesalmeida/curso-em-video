# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

p1 = int(input('primeiro segmento: '))
p2 = int(input('segundo segmento: '))
p3 = int(input('terceiro segmento: '))

if p1 < p2 + p3 and p2 < p1 + p3 and p3 < p1 + p2:  #Condição alinhada, forma segmentos if - if - elif
    print('Os segmentos acima podem formar um triângulo ', end='')
    if p1 == p2 == p3:
        print('Equilatero')
    elif p1 != p2 != p3 != p1:    # != diferente
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Os Segmentos acima não podem formar um triângulo')