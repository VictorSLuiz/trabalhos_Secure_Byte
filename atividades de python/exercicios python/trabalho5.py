# Pede o valor do produto
valor_produto = float(input("Qual o valor do produto? R$ "))

# Pede o percentual de desconto
percentual_desconto = float(input("Qual o percentual de desconto? (ex: 10 para 10%) "))

# Calcula o valor do desconto
valor_desconto = (percentual_desconto / 100) * valor_produto


# Calcula o valor final com desconto
valor_com_desconto = valor_produto - valor_desconto
# Mostra os resultados
print(f"Valor original: R$ {valor_produto:.2f}")
print(f"Desconto: {percentual_desconto}%")
print(f"Valor com desconto: R$ {valor_com_desconto:.2f}")