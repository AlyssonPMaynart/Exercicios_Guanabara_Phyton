#manipulação de str (indicar nome com letra maiuscula e minuscula, quantas letras tem o nome completo e apenas o primeiro nome.

frase = str(input("informe seu nome completo: ")).strip()
print(f"Seu nome em maiúsculo é {frase.upper()}." )
print(f"Seu nome em minúsculo é {frase.lower()}." )
print(f"seu nome tem ao todo {len(frase) - frase.count(' ')} letras. ")
dividido = frase.split()
print(f"Seu primeiro nome possui {len(dividido[0])} letras. "),