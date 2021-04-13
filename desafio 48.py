s = 0
i = 0
for c in range(1, 501, 2):
    if c%3==0:
     s += c
     i += 1
print(i)
print(f'A soma de todos os numeros impares multiplos de 3 e {s}')   