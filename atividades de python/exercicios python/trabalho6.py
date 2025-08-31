valor_principal = float(input("Digite o valor principal (R$): "))


taxa_juros = float(input("Digite a taxa de juros (% ao ano): "))


anos = int(input("Digite o número de anos: "))


montante = valor_principal + (valor_principal * taxa_juros * anos / 100)

print(f"\nValor principal: R$ {valor_principal:.2f}")
print(f"Taxa de juros: {taxa_juros}% ao ano")
print(f"Tempo: {anos} anos")
print(f"Montante final: R$ {montante:.2f}")
