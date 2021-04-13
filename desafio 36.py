from os import system
system('cls')
print('===== \033[32mDESAFIO 36\033[m ===== ')
casa = float(input('Quanto vale a casa: '))
salario = float(input('Quanto voce recebe: '))
ano = int(input('Por quantos anos voce vai pagar: '))
valor = casa / (ano*12)
print('Para pagar uma casa de {} em {} anos a prestacao sera de {:.2f}'.format(casa, ano, valor))
if valor >= salario*(30/100):
    print('Emprestimo \033[31mnegado\033[m')
else:
    print('O seu emprestimo teve \033[32msucesso\033[m')
print('Tenha um Bom dia!')
input()