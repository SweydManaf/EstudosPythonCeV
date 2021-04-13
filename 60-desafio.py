n = int(input('Informe um numero: '))
i = 0
f = n
print(f'{n}! = ', n, end = ' x ')
while i == 0:
    if n != 2:
        print(n-1,  end = ' x ')
    n = n-1
    f = f * n

    if n == 1: 
        i = 1
print(f'1 = {f}')
    
    