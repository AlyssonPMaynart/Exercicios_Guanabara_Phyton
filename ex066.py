soma = cont = 0
while True:
    n = int(input('Informe um número inteiro (999 para parar): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Foram digitados {cont} números e sua soma perfaz {soma}')