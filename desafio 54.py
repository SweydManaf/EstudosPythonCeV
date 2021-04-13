from datetime import date
y = date.today().year
s = 0 
n = 0
for c in range(0, 7):
    ano = int(input('Informe o seu ano de nascimento: '))
    if y - ano >= 21:
        s += 1
    else:
        n +=1
print(f'\nExistem {s} que ja atigiram a maioridade.')
print(f'Existem {n} que ainda nao atingiram a maioridade.')        