print('-='*10)
print('Simulador de Caixa eletrônico')
print('-='*10)
nota50 = nota20 = nota10 = nota1 = 0
while True:
    valor = int(input('Qual valor você quer sacar? '))
    while valor >= 50:
        valor -= 50
        nota50 += 1
    while valor >= 20:
        valor -= 20
        nota20 += 1
    while valor >= 10:
        valor -= 10
        nota10 += 1
    while valor >= 1:
        valor -= 1
        nota1 += 1
    if valor == 0:
        break
if nota50 > 0:
    print(f'Total de {nota50} cédulas de R$50')
if nota20 > 0:
    print(f'Total de {nota20} cédulas de R$20')
if nota10 > 0:
    print(f'Total de {nota10} cédulas de R$10')
if nota1 > 0:
    print(f'Total de {nota1} cédulas de R$1')
print('Volte sempre ao Banco CEV! Tenha um Bom dia!')