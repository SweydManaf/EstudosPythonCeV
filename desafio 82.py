n = []
p = []
i = []
while True:
    n.append(int(input('Digite um numero: ')))
    while True:
        q = str(input('Quer continuar? [S/N] ')).upper()
        if q in 'SN':
            break
    if q == 'N':
        break
for numeros in n:
    if numeros%2==0:
        p.append(numeros)
    else:
        i.append(numeros)
print('-='*30)
print(f'A lista completa e {n}')
print(f'A lista de pares e {p}')
print(f'A lista de impares e {i}')
