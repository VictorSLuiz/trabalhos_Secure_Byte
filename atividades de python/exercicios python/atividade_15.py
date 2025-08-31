valor_original = float(input("Digite o valor do produto (em R$):"))

if valor_original > 100:
    desconto = valor_original * 0.10 
    valor_com_desconto = valor_original - desconto 
    print(f"Voce recebeu um desconto de R$ {desconto:.2f}.")
    print(f"Valor com desconto: R$ {valor_com_desconto:.2f}")
else:
    print("Sem desconto aplicado.")
    print(f"Valor final: R$ {valor_original:.2f}")

