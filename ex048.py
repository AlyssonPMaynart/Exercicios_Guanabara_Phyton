somaMultiplosDeTres = 0
quant = 0
for i in range(1,501,2):
    print(i)
    if i % 3 == 0:
        quant += 1
        somaMultiplosDeTres += i
print('A soma de todos os números ímpares múltiplos de 3 entre 0 a 500 é igual a {}'.format(somaMultiplosDeTres))
print(quant)
