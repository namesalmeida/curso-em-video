# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
# while = enquanto

sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0] #strip é para eliminar espaços
while sexo not in 'MmFf':   # A validação ocorre ao digitar o sexo, se for diferente de Mm ou Ff ele retorna a pergunta.
                            # not in > não estiver em
    sexo = str(input('Dados invalidos. Informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
