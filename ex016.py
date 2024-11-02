#Exercício importação de biblioteca
from math import trunc
n = float(input('Informe um número real: '))
int = trunc(n)
print('O valor inteiro do número {:.2f} é {}'.format(n, int))