# Soma de números inteiros pares, apartir do imput do usuário.

soma = 0
for i in range(1,7):
    num = int(input('Digite um numero inteiro: '))
    if num % 2 == 0:
        soma += num
print('A soma de todos os numero pares é igual a {}'.format(soma))


