n = []
while True:
    n.append(int(input('Digite um valor: ')))
    while True:
        q = str(input('Quer continuar? [S/N] ')).upper()
        if q in 'SN':
            break
    if q == 'N':
        break
print('-='*30)
print(f'Voce digitou {len(n)} elementos')
n.sort(reverse=True)
print(f'Os valores em ordem decrescente sao {n}')
if 5 in n:
    print('O valor 5 faz parte parte da lista') 
else:
    print('O valor 5 nao foi encontrado na lista!') 