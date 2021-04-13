p = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razao: '))
v = p+r
print(p, end = '; ')
for c in range(0, 9):
    print(v, end = '; ')
    v += r
    
#Guanabara soluction
'''
primeiro = int(input('Primeiro numero:'))
razao = int(input('Razao: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(f'{c}', end = ' -> ')
print('ACABOU')
'''
