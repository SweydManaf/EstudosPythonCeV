frase = str(input('Digite a frase: ')).upper().strip()
frase = frase.replace(' ', '')
inverso = frase[::-1]
print(f'O inverso de {frase} e {inverso}')
if frase == inverso:
    print('A frase digitada e palindromo')
else:
    print('A frase digitada nao e um palindromo')
