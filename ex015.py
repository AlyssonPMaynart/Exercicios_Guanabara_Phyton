d = int(input('Informe por quantos dias o veiculo esteve alugado: '))
km = float(input('Informe quantos kilômetros o veiculo percorreu: '))
preco = (d * 60) + (km * 0.15)
print(f'Estando alugado por {d} dias e rodando {km}km, o aluguel do veiculo custará R${preco}')
