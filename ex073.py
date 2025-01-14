tabela = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional',
          'São Paulo', 'Corinthias', 'Bahia', 'Cruzeiro', 'Vasco',
          'Vitória', 'Athletico', 'Fluminense', 'Grêmio', 'Juventude',
         'Bragantino', 'Athletico-PR', 'Criciúma', 'Athlético-GO', 'Cuiabá')
print('-=' * 15)
print(f'TABELA DO BRSILEIRÃO 2024: {tabela}')
print('-=' * 15)
print(f'Os 5 primeiro colocados são {tabela[0:5]}')
print('-=' * 15)
print(f'Os 4 ultimos colocados são {tabela[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-=' * 15)
print(f'O Bahia está na {tabela.index('Botafogo')+1}ª posição')