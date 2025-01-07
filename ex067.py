cont = 1
resultado = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-=' * 10)
    if n < 0:
        break
    else:
        cont = 1
    while cont < 11:
        resultado = n * cont
        print(f'{n} X {cont} = {resultado}')
        cont += 1
    print('-=' * 10)
print('PROGRAMA ENCERRADO. Volte Sempre!')
