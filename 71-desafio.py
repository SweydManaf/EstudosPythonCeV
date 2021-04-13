nome = 'BANCO CEV'
print('='*25)
print(f'{nome:^25}')
print('='*25)
valor = int(input('Que valor quer sacar? '))
c50 = valor // 50
if c50 != 0:
    
    print(f'Total de {c50} cedulas de 50')
    valor = valor - (c50*50)
c20 = valor // 20
if c20 != 0:
    print(f'Total de {c20} cedulas de 20')
    valor = valor - (c20*20)
c10 = valor // 10
if c10 != 0:
    print(f'Total de {c10} cedulas de 10')
    valor = valor - (c10*10)
if valor > 0:
    print(f'Total de {valor} cedulas de 1')
print('='*25)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')