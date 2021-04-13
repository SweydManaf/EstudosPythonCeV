maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Informe o peso da {c}: '))
    if c == 1:
        menor = peso
        maior = peso
    else:    
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O menor peso e {menor}')
print(f'O maior peso e {maior}')
