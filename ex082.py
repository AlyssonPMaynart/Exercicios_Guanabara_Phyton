valores = []
impar = []
par = []
while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'A lista completa é {valores}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')

    