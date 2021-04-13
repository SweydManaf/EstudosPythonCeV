pessoas = list()
pessoa = dict()
while True:
    pessoa['nome'] = str(input('Nome: ')).capitalize()
    while True:
        pessoa['sexo'] = str(input('Sexo: ')).upper()
        if pessoa['sexo'] == 'M' or pessoa['sexo'] == 'F':
            break
        else:
            print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    while True:
        q = str(input('Quer continuar? [S/N]: ')).upper()
        if q == 'S' or q == 'N':
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    if q == 'N':
        break
print('-='*30)
print(f'A) O grupo tem {len(pessoas)} pessoas.')
media = 0
for c, i in enumerate(pessoas):
    media +=  pessoas[c]['idade'] 
media = media / len(pessoas)
print(f'B) A media de idade do grupo e de {media}')
print(f'C) As mulheres cadastradas foram:', end = ' ')
for c in range(0, len(pessoas)):
    if pessoas[c]['sexo'] == 'F':
        print(pessoas[c]['nome'], end = ' ')
print('\nD) Lista das pessoas que estao acima da media: ')
for c in range(0, len(pessoas)):
    if pessoas[c]['idade'] > media:
        print()
        for k, v in pessoas[c].items():
            print(f'{k} = {v}', end = '; ')
print('\n< < < ENCERRADO > > >')
