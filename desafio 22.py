from os import system
system('cls')
print('===== DESAFIO 22 =====')

nome = str(input('Informe seu nome completo: ')).strip()
print('='*30)
print(nome.upper(), ' - Seu nome tudo maiusculo')
print(nome.lower(), ' - Seu nome todo minusculo')
print(len(nome) - nome.count(' '), ' - Quantidade de letras')
# print(nome.find(' '), ' - Quantidade de letras do primeiro nome')
nome1 = nome.split()
print(len(nome1[0]), ' - Quatidada de letras do primeiro nome')

print('='*30)

