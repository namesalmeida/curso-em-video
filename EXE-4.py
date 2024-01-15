a = input('Digite algo: ')
print('O primitivo desse valor é ', type(a))
print('Só tem espacos? ', a.isspace()) #se tem espaço > o (a.) é sempre objeto o is é metodo
print('É um número? ', a.isnumeric()) #se é numerico
print('É alfabético? ', a.isalpha()) #se é alfabetico
print('É alfanumérico? ', a.isalnum()) #se é alfanumerico
print('Está em maiúscula? ', a.isupper()) #se é maiuscula
print('Está em minúscula? ', a.islower()) #se é minuscula
print('Está capitalizada? ', a.istitle()) #nem maicula nem minuscula