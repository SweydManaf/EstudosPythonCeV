from os import system
system('cls')
aluno = []
while True:
    nome = str(input('Nome: ')).capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    aluno.append([nome,[nota1, nota2], [((nota1+nota2)/2)]])
    while True:
        q = str(input('Quer continuar? [S/n]: ')).upper()
        if q in 'SN':
            break
    if q == 'N':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*25)
for c in range(0, len(aluno)):
    print(f'{c:<4}{aluno[c][0]:<10}{aluno[c][2][0]:>8.1f}')
print('-='*30)
 
fim = 0
while fim != 999:
    while True:
        fim = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
        if fim >= len(aluno) and fim != 999:
            print('Aluno inexistente')
        else:
            break
    if fim == 999:
        break
    print(f'Notas de {aluno[fim][0]} sao {aluno[fim][1]}')
    print('='*30)
print('FINALIZANDO')
print('Volte sempre')

#Colocar no YouTube