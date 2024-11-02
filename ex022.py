#manipulação de str (indicar nome com letra maiuscula e minuscula, quantas letras tem o nome completo e apenas o primeiro nome.

frase = str(input("informe seu nome completo: ")).strip()
print('Seu nome em maiúsculo é {}.' .format(frase.upper()))
print('Seu nome em minúsculo é {}.'.format(frase.lower()) )
print('Seu nome tem ao todo {} letras. '.format(len(frase) - frase.count(' ')))
divididoPorPalavra = frase.split()
print("Seu primeiro nome possui {} letras." .format(len(divididoPorPalavra[0]))),

print(frase[:5])