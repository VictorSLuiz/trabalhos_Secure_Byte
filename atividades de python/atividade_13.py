print('VERIFICADOR DE DIVISIVEIS POR 3 E 5')
print('-----------------------------------')
print('DIGITE UM NÚMERO :')
n1 = int(input()) 

if n1 % 3 == 0 and n1 % 5 == 0 :
    print(f'{n1} é divisível')
else :
    print(f'{n1} não é divisível')
