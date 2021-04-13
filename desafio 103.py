def ficha(nome='', gols=''):
    if nome.strip() == '':
        nome = '<desconhecido>'
    if gols.strip() == '':
        gols = 0
    return f'O {nome} fez {gols} gol(s) no campeonato.'


#Programa Principal
nome = str(input('Nome do jogador: '))
gols = str(input('Numero de Gols: '))
print(ficha(nome, gols))

#Colocar no YouTube