# se carro.esquerda() é igual a ifcarro.esquerda(): > if para estrutura simples
# senão               é igual a else:               > else para estrutura composta


tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo'if tempo <=3 else 'carro velho')
print('--FIM--')

#------------------------------------------------------------------

nome = str(input('Qual é o seu nome? '))
if nome == 'names':
    print('Que nome lindo voce tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}'.format(nome))

#------------------------------------------------------------------

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua media foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABENS!')
else:
    print('Sua media foi ruim! ESTUDO MAIS MALA!')

#-------------------------------------------------------------------

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
M = (n1 + n2)/2
print('A sua media foi {:.1f}'.format(m))
print('PARABENS' if m >=6 else 'ESTUDE MAIS')'''