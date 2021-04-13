aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Media de {aluno["Nome"]}: '))
if aluno['Media'] >= 7:
    aluno['Situacao'] = 'Aprovado'
elif aluno['Media'] < 7 and aluno['Media'] > 5:
    aluno['Situacao'] = 'Suficiente'
else:
    aluno['Situacao'] = 'Reprovado'
print('-='*30)
for k, v in aluno.items():
    print(f'{k} e igual a {v}')
    