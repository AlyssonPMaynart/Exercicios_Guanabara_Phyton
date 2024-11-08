# Operações matemáticas usando while
print('-----------------')
print('Mini Calculadora')
print('-----------------')
n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
escolha = 0
multiplicacao = 0
while escolha != 5:
    print('[1] somar\n'
          '[2] multiplicar\n'
          '[3] maior\n'
          '[4] novos numeros\n'
          '[5] sair do programa')
    escolha = int(input('>>>>>>>>>>>>>Escolha um número dentre as opções: '))
    if escolha == 1:
        soma = n1 + n2
        print('A soma entre {} e {} vale {}'.format(n1, n2, soma))
    elif escolha == 2:
        multiplicacao = n1 * n2
        print('A multiplicação entre {} e {} vale {}'.format(n1, n2, multiplicacao))
    elif escolha == 3:
        if n1 > n2:
            print('o maior numero entre {} e {} é {}'.format(n1, n2, n1))
        elif n1 == n2:
            print('Os numeros são iguais')
        else:
            print('o maior numero entre {} e {} é {}'.format(n1, n2, n2))
    elif escolha == 4:
        n1 = int(input('Informe o primeiro valor: '))
        n2 = int(input('Informe o segundo valor: '))
    elif escolha == 5:
        print('Fim do programa! Volte sempre!')
    else:
        print('opção invalida. Tente novamente')
    print('=-=' *10)


