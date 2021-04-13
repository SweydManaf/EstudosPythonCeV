'''
m18 - maiores de 18
h - homens
m20 - mulheres menos de 20 
'''
m18 = h = m20 = 0 
while True:    
    print('-'*25)
    print('CADSTRE UMA PESSOA')
    print('-'*25)
    
    idade = int(input('Idade: '))
    if idade > 18:
        m18 += 1
    while True:
        sexo = str(input('Sexo: [M/F] ')).upper()
        if sexo in 'MF':
            break 
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade < 20:
        m20 += 1 
    while True:
        print('-'*25)
        variavel = str(input('Quer continuar [S/N]: ')).upper()
        if variavel in 'SN':
            break
    if variavel == 'N':
        break
    
print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoas com mais de 18 anos: {m18}')
print(f'Ao todo temos {h} homens cadastrados')
print(f'E temos {m20} mulheres com menos com menos de 20 anos')