from random import randint
numero = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)

print(f'Os valor sorteados foram: ', end = '')
for n in numero:
    print(n, end = ' ')
print(f'\nO maior valor sorteado foi {max(numero)}')
print(f'O menor valor sorteado foi {min(numero)}')
