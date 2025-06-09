print('VERIFICADOR DE DIVISIVEIS POR 3 E 5')
print('-----------------------------------')
print('DIGITE UM NÚMERO :')
n1 = int(input()) 

if n1 % 3 == 0 and n1 % 5 == 0 :
    condicao = ('é divisível')
else :
    condicao = ('não é divisível')

print(f'{n1} {condicao} por 3 e por 5 ')

