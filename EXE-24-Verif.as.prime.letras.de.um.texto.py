'''strip > retira os espaços
upper > tudo maiuscula'''

cid = str(input('Em que cidade voce nasceu? ')).strip()
print(cid[:5].upper() == 'SANTOS')