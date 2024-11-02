#seno, cosseno e tangente a partir de um ângulo informado pelo usuário.
from math import tan,sin,cos,radians
ang = int(input('Indique um ângulo qualquer: '))
sen = float(sin(radians(ang)))
cos = float(cos(radians(ang)))
tang = float(tan(radians(ang)))
print('Um angulo de {}° possui um seno de {:.2f}°, um cosseno de {:.2f}° e uma tangente de {:.2f}°'.format(ang, sen, cos, tang))