#Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Indique um número inteiro para conversão: '))
conv = int(input("Indique a base que deseja converter o número \n"
      "[1] converter para Binário\n"
      "[2] converter para OCTAL\n"
      "[3] converter para HEXADECIMAL\n"
      "Sua Opção: "))
if conv== 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(bin(num)[2:]))
elif conv == 2:
    print('{} convertido para OCTAL é igual a {}'.format(oct(num)[2:]))
elif conv == 3:
    print('{} convertio para HEXADECIMAL é igual a {}'.format(hex(num)[2:]))
else:
    print("Você é burro? Opção inválida")