#cálculo do valor da hipotenusa
import math
catetoOposto = float(input('Informe em cm o tamanho do cateto oposto: '))
catetoAdjacente = float(input('Informe em cm o tamanho do cateto adjacente: '))

hipotenusa = math.hypot(catetoOposto, catetoAdjacente)

print('Um triângulo cujo cateto maior possui {}cm e o cateto menor possui {}cm, a hipotenusa terá {:.1f}cm'.format(catetoOposto, catetoAdjacente, hipotenusa))