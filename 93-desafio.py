jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do joador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c}: ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for p, g in enumerate(jogador['gols']):
    print(f'    => Na partida {p}, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} golos')
