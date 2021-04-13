'''
n = []
nc = n[:]
c = 0
while True:
    n.append(int(input('Digite um valor: ')))
    if n[c] in nc:
        print('Valor duplicado nao vou adicionar')
        n.remove(n[c])
    else:
        nc.append(n[c])
        print('Valor adicionado com sucesso...')
        c+=1
    while True:
        q = str(input('Quer continuar? [S/N] ')).upper()
        if q in 'SN':
            if q == 'S':
                break
            elif q == 'N':
                break
    if q == 'N':
        break
print('-='*30)
nc.sort()
print(f'Voce digitou os valores {nc}')
input()
'''
#Guanabara soluction
numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Valor duplicado! Nao vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-='*30)
numeros.sort()
print(f'Voce digitou os valores {numeros}')