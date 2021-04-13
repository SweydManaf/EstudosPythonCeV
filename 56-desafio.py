idadet = 0
m = 0 
n = 0
for c in range(1, 5):
    print(f'----- {c} a PESSOA -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M] ou [F]: ')).upper()
    idadet = idade + idadet 
    if sexo == 'M':    
        if idade > m:
            m = idade
            nomem = nome 
    if sexo == 'F':
        if idade < 20:
            n += 1
idadet = idadet / 4

print(f'A media da idade do grupo e {idadet}')
print(f'O {nomem} e o homem mais velho.')
print(f'Existem {n} mulheres com menos de 20 anos')