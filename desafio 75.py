numeros = (int(input('Digite um numero: ')),
          int(input('Digite outro numero: ')),
          int(input('Digite mais um numero: ')),
          int(input('Digite o ultimo numero: ')))
print(f'Voce digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}a posicao')
else:
    print(f'O valor 3 nao foi digitado em nunhuma posicao')
print(f'Os valores pares digitados foram ', end = '')
for c in numeros:
    if c % 2 == 0:
        print(c, end = ' ')
