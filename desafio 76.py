lista = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 25.00,
         'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-'*40)
print(f'{"Listagem de precos":^40}')
print('-'*40)
c = 0
while True:
    print(f'{lista[c]:.<30}R$ ', end = ' ')
    print(f'{lista[c+1]:>7.2f}')
    c+=2
    if c == 18:
        break