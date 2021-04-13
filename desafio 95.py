jogadores = list()
jogador = dict()
gols = list()

#RECOLHA DE DADOS
while True:
    print('-'*30)
    jogador['nome'] = str(input('Nome do joador: ')).capitalize()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {c+1}: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    gols.clear()
    while True:
        q = str(input('Quer continuar? [S/N] ')).upper()
        if q == 'S' or q == 'N':
            break
    if q == 'N':
        break
#########################################################
print('-='*30)
print('cod ', end= '')
for i in jogador.keys():
    print(f'{i:<15}', end= '')
print()
print('-'*40)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end ='')
    print()
print('-'*40)
#GUANABARA SOLUCTION
##########################################################
while True:
    while True:
        n = int(input('Mostrar dados de qual jogador(999 para parar)? '))
        if n == 999:
            break
        if n < len(jogadores):
            break
        else:
            print(f'ERRO! Nao existe jogador com codigo {n}! Tente novamente')
    print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[n]["nome"]}: ')
    for c in range(0, len(jogadores[n]['gols'])):
        print(f'    No jogo {c+1} fez {jogadores[n]["gols"][c]}')
    break