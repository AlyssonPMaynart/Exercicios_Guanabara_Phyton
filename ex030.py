n = int(input('Digite um numero intéiro: '))
div = n % 2
if div == 0:
    print('O número {} é par'.format(n))
else:
    print('O número {} é impar'.format(n))