n = int(input('Informe um numero inteiro [999 para encerrar o programa]: '))
cont = 0
total = 0
while n!= 999:
    cont += 1
    total = total + n
    n = int(input('Informe um numero inteiro [999 para encerrar o programa]: '))
print('Fim do Programa. Foram digitados {} numeros cuja soma perfaz o valor de {}'.format(cont, total))