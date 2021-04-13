galera = list()
info = list()
cadastro = 0
while True:
    info.append(str(input('Nome: ')))
    info.append(float(input('Peso: ')))
    galera.append(info[:])
    info.clear()
    cadastro += 1
    while True:
        q = str(input('Quer continuar? [S/N] ')).upper()
        if q in 'SN':
            break
    if q == 'N':
        break
print('-='*30)
maior = menor = 0
c = 0
for peso in galera:
    if c == 0:        
        maior = peso[1]
        menor = peso [1]
        c+=1
    else:
        if peso[1] >= maior:
            maior = peso[1]
        elif peso[1] < menor:
            menor = peso[1]
print('Ao todo, voce cadastrou 5 pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end = '')
for nome in galera:
    if nome[1] == maior:
        print(nome[0], end = ' ')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end = '')
for nome in galera:
    if nome[1] == menor:
        print(nome[0], end=' ')