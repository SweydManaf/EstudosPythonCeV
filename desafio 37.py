from os import system
system('cls')

n = int(input('Informe um numero inteiro: '))
print('\n===== CONVERSOS DE BASES NUMERICAS =====')
print('''1 - Para binario
2 - Para octal
3 - Para hexadecimal''')
d = int(input('Desejo: '))
if d == 1:
    print('O seu numero em binario e {}'.format(bin(n).replace('0b', '')))
elif d == 2:
    print('O seu numero em octal e {}'.format(oct(n).replace('0o', '')))
elif d == 3:
    print('O seu numero em hexadecimal e {}'.format(hex(n).replace('0x', '')))
else:
    print('Da proxima informe uma opcao valida.')