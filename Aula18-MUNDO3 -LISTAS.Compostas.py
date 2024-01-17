''' a = ["p", "y", "t", "h", "o", "n"]
print(a[:6])'''
teste = list()
teste.append('Names')
teste.append(36)
galera = list()
galera.append(teste[:])
teste[0] = 'Karine'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = (['Names',36], ['karine', 31], ['karyn', 7])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
#--------------------------------------------------------------

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):     # incluir apenas 3 pessoas
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()            # clear > para limpar ou invalidar o cache

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
