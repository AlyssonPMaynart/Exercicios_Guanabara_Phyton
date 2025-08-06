def área(largura, comprimento):
    área = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {área}m².')

# Programa principal
print('Controle de Terrenos')
print('-' * 20)
área(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))