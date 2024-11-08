# Cálculo de média
n1 = float(input('Informe a nota da primeira unidade: '))
n2 = float(input('Informe a nota da segunda unidade: '))
média = (n1 + n2) / 2
print('A média do aluno é {:.1f}'.format(média))
if média >= 6.0:
    print('Sua média foi boa, PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')