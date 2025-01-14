compras = ("Arroz", 5.99,
           "Feijão", 4.50,
           "Macarrão", 3.25,
           "Leite", 6.00,
           "Pão", 4.75,
           "Café", 10.30,
           "Açúcar", 2.80,
           "Óleo", 7.90,
           "Sal", 1.50,
           "Manteiga", 9.60)
print('-'*40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(compras)):
    if pos % 2 == 0:
        print(f'{compras[pos]:.<30}', end='')
    else:
        print(f'R${compras[pos]:.2f}')
print('-'*30)