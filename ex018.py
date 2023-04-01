#seno, cosseno e tangente a partir de um ângulo informado pelo usuário.
from math import tan,sin,cos,radians
ang = int(input('Indique um ângulo qualquer: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tang = tan(radians(ang))
print(f'Um angulo de {ang}° possui um seno de {sen:.2f}°, um cosseno de {cos:.2f}° e uma tangente de {tang:.2f}°')
