from datetime import date
year = date.today().year
pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = -(int(input('Ano de nascimento: '))) + 2020
pessoa['ctps'] = int(input('Carteira de Trabalho (0 nao tem): '))
if pessoa['ctps'] > 0:
    pessoa['contratacao'] = int(input('Ano de contratacao: '))
    pessoa['salario'] = float(input('Salario: '))
    pessoa['aposentadoria'] = (pessoa['contratacao']+35) - (year - pessoa['idade'])
print('-='*30)
for k, v in pessoa.items():
    print(f'- {k} tem o valor {v}')
    