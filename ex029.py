vel = float(input('Informe a velocidade do veículo em km: '))
multa = (vel - 80)*7
if vel > 80:
    print('MULTADO! Velocidade excedeu o limite permitido, sua multa é de R${:.2F}'.format(multa))
print('=== Fim do Programa === ')