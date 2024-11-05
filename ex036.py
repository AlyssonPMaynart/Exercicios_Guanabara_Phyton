print('-='*15)
print('ANÁLISE DE EMPRÉSTIMO BANCÁRIO')
print('-='*15)
imovel = float(input("Informe o valor do imóvel desejado: R$ "))
salario = float(input("Informe o valor de sua remuneração: R$ "))
anos = int(input("Informe em quantos anos pretende quitar o empréstimo: R$ "))
prestação = imovel / (anos * 12)
if prestação <= salario * 0.3:
    print('Parabéns, seu emprestimo foi aprovado!')
else:
    print('Valor da prestação excede 30% de sua renda. EMPRESTIMO NEGADO')