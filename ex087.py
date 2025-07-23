matriz = [[0, 0, 0], [0, 0,0], [0,0,0]]
somaPares = 0
somaTer = 0
maiorSeg = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' *30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somaPares += matriz[l][c]
    print()
print('-=' *30)
print(somaPares)
for l in range(0,3):
    somaTer += matriz[l][2]
print(somaTer)
for c in range(0,3):
    if c == 0:
        maiorSeg = matriz[1][c]
    elif matriz[1][c] > maiorSeg:
        maiorSeg =matriz[1][c]
print(maiorSeg)

#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
