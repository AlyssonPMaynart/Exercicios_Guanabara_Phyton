#gasto de tinta de acordo com o tamanho da parede. Obs.: 1L de tinta pinta 2m²
a = float(input('Qual a altura da parede em metros? '))
l = float(input('Qual a largura da parede em metros? '))

litro = (a * l) / 2

print(f'São necessários {litro} litros de tinta para pintar a parede com as dimensões informadas')