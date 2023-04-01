salario = float(input('Informe o valor de seu salário:R$ '))
if salario > 1250:
    print(f'Seu salario reajustado ficou em R${salario*1.15:.2f}')
else:
    print(f'Seu salário reajustado ficou em R${salario*1.1:.2f}')