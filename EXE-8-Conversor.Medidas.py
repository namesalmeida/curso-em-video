# com casas decimais > de metros para centimetros e milimetros
medida = float(input('Uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {}cm e {}mm'.format(medida, cm, mm))

# sem casas decimais
medida = float(input('Uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))
