# Cálculo de média
n1 = float(input('Informe a nota da primeira unidade: '))
n2 = float(input('Informe a nota da segunda unidade: '))
média = (n1 + n2) / 2
print(f'A média do aluno é {média:.1f}')
print('Sua média foi boa, PARABÉNS!' if média >= 6.0 else 'Sua média foi ruim! ESTUDE MAIS!')

