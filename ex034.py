salario = float(input('Informe o valor de seu salário:R$ '))
if salario < 1250:
    print('Seu salario reajustado ficou em R${:.2f}'.format(salario * 1.15))
else:
    print('Seu salário reajustado ficou em R${:.2f}'.format(salario * 1.1))