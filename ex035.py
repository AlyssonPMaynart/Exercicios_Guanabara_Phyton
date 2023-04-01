r1 = float(input('Informe o tamanho da primeira reta: '))
r2 = float(input('Informe o tamanho da segunda reta: '))
r3 = float(input('Informe o tamanho da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os trê segmentos de reta informados formam um triângulo')
else:
    print('Os trê segmentos de reta informados NÃO formam um triângulo')