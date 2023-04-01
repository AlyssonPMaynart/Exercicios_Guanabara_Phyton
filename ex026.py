frase = str(input('Digite uma Frase ')).upper().strip()
print(f"A frase possui {frase.count('A')} letras A")
print(f"A primeira letra A aparece na posição {frase.find('A')+1} ")
print(f"A última letra A aparece na posição {frase.rfind('A')+1} ")