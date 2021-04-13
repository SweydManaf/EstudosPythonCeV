'''
n = 1
while n == 1:
    sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()
    if sexo in 'M F':
        n = 2
    else:
        print('Digite novamente M para masculino e F para feminino.')
'''
        
sexo = str(input('Informe seu sexo: [M/F]: ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()
print(f'Sexo {sexo} registrado com sucesso')