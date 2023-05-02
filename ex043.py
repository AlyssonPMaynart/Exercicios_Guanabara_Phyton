peso = float(input("Informe seu peso em kg: "))
altura = float(input("Informe su altura em metros: "))
imc = peso / (altura * altura)
altura_cm = altura * 100
print(f"O IMC dessa pessoa é {imc:.1f}")
if imc < 18.5:
    print("Abaixo do Peso")
elif 18.5 <= imc < 25:
    print("Peso Ideal")
elif 25 <= imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 40:
    print("Obesidade")
else:
    print("OBESIDADE MÓRBIDA")