lista = [[], []]
for n in range(0,7):
    num = (int(input(f'Digite o {n+1}º número: ')))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(f'Os numeros pares digitados foram: {lista[0]}')
print(f'Os numeros impares digitados foram: {lista[1]}')