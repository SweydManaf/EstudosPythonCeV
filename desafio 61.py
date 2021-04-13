termo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razao da PA: '))
v = termo + razao
i = 0
print(termo, end = '; ')
while i < 9:
    print(v, end = '; ')
    v += razao
    i += 1
print('ACABOU')