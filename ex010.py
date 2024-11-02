#conversão de real em dólar. Com valor do dólar definida pelo usúario.
real = float(input('informe quantos reais você pretende converter para dolar?: R$'))
dolar = float(input('Informe a atul cotação do Dólar'))

conver = real / dolar

print(f'Com R${real} é possível comprar U$${conver:.2f} ')

print('Com R${:.2f}, é possivel comprar U$${:.2f}'.format(real, conver))