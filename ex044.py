print("Lojas Macopinoua")

preco = float(input("Informe o valor da compra:R$ "))
forma_de_pagamento = int(input("Indique a forma de pagamento: \n"
                               "[1] À Vista dinheiro/cheque\n"
                               "[2] À Vista cartão\n"
                               "[3] 2x no cartão \n"
                               "[4] 3x ou mais no cartão"
                               "Sua Opção: "))
if forma_de_pagamento == 1:
    preco_corrigido = preco * 0.9
elif forma_de_pagamento == 2:
    preco_corrigido = preco * 0.95
elif forma_de_pagamento == 3:
    preco_corrigido = preco
elif forma_de_pagamento == 4:
    preco_corrigido = preco * 1.20
else:
    preco_corrigido = preco
    print("Opção inválida, tente novamente!")

print(f" Nesta modalidade de pagamento, a compra que custou R${preco} passa a custar R${preco_corrigido} ")
