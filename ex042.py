r1 = float(input('Informe o tamanho da primeira reta: '))
r2 = float(input('Informe o tamanho da segunda reta: '))
r3 = float(input('Informe o tamanho da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os trê segmentos de reta informados formam um triângulo ')
    if r1 == r2 == r3:
        print('Todos os lados são iguais, o triângulo é EQUILÁTERO')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r3 == r2 != r1:
        print('Dois lados iguais e um diferente, o triângulo é ISÓSCELES')
    else:
        print('Todos os lados diferentes, o triângulo é ESCALENO')
else:
    print('Os trê segmentos de reta informados NÃO formam um triângulo')
