while True :
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('='*30)
    if n > 0:
        for c in range(1, 11):
            print(f'{n} x {c} = {n*c}')
    else:
        break
print('Programa TABUADA ENCERRADO. Volte sempre!')
