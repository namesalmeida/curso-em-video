sal = float(input('Qual é o salario do funcionario? R$ '))
perc = float(input('Pecentual de aumento: '))
novo = sal + (sal * 15 / 100)
print('O novo salario sera de {:.2f} com aumento de {:.0f}%'.format(novo, perc))
