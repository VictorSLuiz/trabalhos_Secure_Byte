negativos = 0

for i in range(4):
    num = float(input(f"Digite o {i+1}º número: "))
    if num < 0:
        negativos += 1

print(f"Você digitou {negativos} número(s) negativo(s).")