matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spares = s3a = 0
for c in range(0,3):
    for l in range(0,3):
        matriz[c][l] = int(input(f'Digite um valor para [{c}, {l}]: '))
        if matriz[c][l]%2 == 0:
            spares += matriz[c][l]
        if l == 2:
            s3a += matriz[c][l]
print('-='*30)
for c in range(0, 3):
    for l in range(0, 3):
        print(f'[{matriz[c][l]:^5}]', end = '')
        if l == 2:
            print()
print('-='*30)
print(f'A soma dos valores pares e {spares}')
print(f'A soma dos valores da terceira coluna e {s3a}')
print(f'O maior valor da segunda coluna e {max(matriz[1])}')
