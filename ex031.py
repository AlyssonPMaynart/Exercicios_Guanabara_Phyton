km = float(input('Informe a distância da viagem em km: '))
if km <= 200:
    print('O preço da passagem é R$ {:.2f}'.format(km*0.5))
else:
    print('O preço da passagem é R$ {:.2f}'.format(km*0.45))