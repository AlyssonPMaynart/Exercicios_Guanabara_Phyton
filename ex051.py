# progressão aritimética
num = int(input('informr um numero inteiro: '))
r = int(input('Informe sua razão: '))
decimo = num + (10 - 1) * r
for i in range(num, decimo + r, r):
    num += r
    print('{}'.format(i), end=' -> ')
print('ACABOU')