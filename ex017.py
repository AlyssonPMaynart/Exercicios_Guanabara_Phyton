#cálculo do valor da hipotenusa
import math
cma = float(input('Informe em cm o tamanho do cateto maior: '))
cme = float(input('Informe em cm o manhao do cateto menor: '))
hip = math.hypot(cma, cme)
print(f'Um triângulo cujo cateto maior possui {cma}cm e o cateto menor possui {cme}cm, a hipotenusa terá {hip:.1f}cm')