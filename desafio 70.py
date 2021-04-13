programa = 'LOJA SUPER BARATAO'
print('-='*25)
print(f'{programa:^40}')
print('-='*25)
t = m1000 = nb = mb = c = 0
while True:
    
    nome = str(input('Informe o nome do produto: '))
    preco = float(input('Informe o preco: '))
    t += preco
    c += 1
    if preco > 1000:
        m1000 += 1
    if c == 1 or preco < nb:
        nb = preco
        mb = nome
    while True:
        variavel = str(input('Quer continuar? [S/N] ')).upper()
        if variavel in 'SN':
            break
    if variavel == 'N':
        break
fim = 'FIM DO PROGRAMA'
print(f'{fim:-^50}')
print(f'O total da compra foi {t}MT')
print(f'Temos {m1000} produtos custanto mais de 1000.00MT ')
print(f'O produto mais barato foi {mb} que custa {nb}')