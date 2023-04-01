km = float(input('Informe a distância da viagem em km: '))
if km <= 200:
    print(f'O preço da passagem é R$ {km*0.5:.2f}')
else:
    print(f'O preço da passagem é R$ {km*0.45:.2f}')