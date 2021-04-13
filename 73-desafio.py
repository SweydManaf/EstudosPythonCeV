times = ('Corinthias', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro',
        'Flamengo', 'Vasco', 'Chapecoense', 'Atletico', 'Botafogo', 
        'Atletico-PR', 'Bahia', 'Sao Paulo', 'Fluminese', 'Sport Recife',
        'EC Vitoria', 'Coritiba', 'Avai', 'Ponte Preta', 'Atletico-GO')
print('-='*25)
print(times)
print('-='*25)
print(f'Os 5 primeiros sao {times[0:5]}')
print('-='*25)
print(f'Os 4 ultimos sao {times[-4:]}')
print('-='*25)
print(f'Os times em ordem alfabetica: {sorted(times)}')
print('-='*25)
print(f'O Chapecoense esta na posicao {times.index("Chapecoense")+1}')
