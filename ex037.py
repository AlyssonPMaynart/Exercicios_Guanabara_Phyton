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
    print(f"{num} convertido para BINÁRIO é igual a {bin(num)[2:]}")
elif conv == 2:
    print(f"{num} convertido para OCTAL é igual a {oct(num)[2:]}")
elif conv == 3:
    print(f"{num} convertio para HEXADECIMAL é igual a {hex(num)[2:]}")
else:
    print("Você é burro? Opção inválida")