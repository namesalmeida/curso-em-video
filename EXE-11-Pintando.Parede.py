L = float(input('Qual é largura da parade? '))
A = float(input('Qual é Altura da parede? '))
Area = L * A
print('Sua parede tema  dimenssão de {} x {} e sua áre é de {}m²'.format(L, A, Area))
tinta = Area / 2
print('Para pintar essa parede, você irá precisar de {}l de tinta'.format(tinta))