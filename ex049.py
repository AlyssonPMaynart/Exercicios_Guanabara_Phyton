#Tabuada com estrutura repetitiva

n1 = int(input('Informe um número: '))
print('Tabuada de {}'.format(n1))
for i in range (1, 11):
    print('{} * {} = {}'.format(i, n1, i *n1))