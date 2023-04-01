vel = float(input('Informe a velocidade do veículo em km: '))
multa = (vel - 80)*7
if vel > 80:
    print(f'MULTADO! Velocidade excedeu o limite permitido, sua multa é de R${multa:2F}')
print('=== Fim do Programa === ')