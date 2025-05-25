valororiginal = float(input("Digite o valor do produto (em R$):"))

if valororiginal > 100:
    desconto = valororiginal * 0.10 
    valor_com_desconto = valororiginal - desconto 
    print(f"Voce recebeu um desconto de R$ {desconto:.2f}.")
    print(f"Valor com desconto: R$ {valor_com_desconto:.2f}")
else:
    print("Sem desconto aplicado.")
    print(f"Valor final: R$ {valororiginal:.2f}")

