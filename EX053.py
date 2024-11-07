#VERIFICAÇÃO PALINDROMO
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
fraseInvertida = junto[::-1]
print('O inverso de {} é {} '.format(junto, fraseInvertida))
if fraseInvertida == junto:
    print('Temos um palíndrdomo')
else:
    print('Não temos um palíndromo')