from datetime import date
ano = int(input("Informe o ano de seu nascimento "))
idade = date.today().year - ano
print('Você tem {} anos'.format(idade))
if idade == 18:
    print("Está no tempo exato para alistamento militar. Procure a junta militar mais proxima!")
elif idade < 18:
    print('Ainda é cedo para se alistar faltam {} anos'.format(18 - idade))
else:
    print('Você passou {} ano(s) do prazo para o alistamento militar, procure a junta militar imediatamente.'.format(idade - 18))