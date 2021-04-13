numeros = []
for c in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a Posicao {c}: ')))
print('-='*30)
print(f'Voce digitou os valor {numeros}')

print(f'O maior valor digitado foi {max(numeros)} nas posicoes', end =' ')
for p, i in enumerate(numeros):
    if max(numeros) == numeros[p]:
        print(p, end='...')

print(f'\nO menor valor digitado foi {min(numeros)} nas posicoes ', end = ' ')
for p, i in enumerate(numeros):
    if min(numeros) == numeros[p]:
        print(p, end='...')

#Colocar no YouTube