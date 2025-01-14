numeros = (int(input('Digite um numero: ')),
           int(input('Digite um numero: ')),
           int(input('Digite um numero: ')),
           int(input('Digite um numero: ')))
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)} posição')
else:
    print('O numero 3 não aparece na tupla')
for n in numeros:
    if n % 2 == 0:
        print(f'Os valores pares digitados foram {n} ', end='')