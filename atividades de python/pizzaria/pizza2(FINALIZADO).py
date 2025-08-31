print('----------------------------------')
print('======= pizzaria meu nobre =======')
print('----------------------------------')
print('')
print('******* SABORES PIZZAS ***********')
print(' CALABRESA , A MODA  ')
print(' 4 QUEIJOS , PORTUGUESA')
print('----------------------------------')
print('======== PIZZAS - TAMANHO ========')
print(' PEQUENA          R$ 20,00        ')
print(' MEDIA            R$ 30,00        ')
print(' GRANDE           R$ 40,00        ')
print('----------------------------------')

print("========= refrigerantes ==========")
print(' COCA-COLA - 2L      R$ 10,00     ')
print(' DOLLY - 1L          R$ 4,00      ')
print(' FANTA - 2L          R$ 8,00      ')
print(' GUARANÁ - 2L        R$ 9,00      ')
print('----------------------------------')
print('')
print('==================================')
print('         FAÇA SEU PEDIDO          ')
print('==================================')
print('         ESCOLHA SUA PIZZA        ')
print('----------------------------------')
print('[1] CALABRESA ')
print('[2] A MODA    ')
print('[3] 4 QUEIJOS ')
print('[4] PORTUGUESA')
print('==================================')
pizza = int(input('DIGITE O NUMERO DA PIZZA ESCOLHIDA: '))
print('')
print('==================================')
print('         ESCOLHA O TAMANHO        ')
print('----------------------------------')
print('P - PEQUENA ')
print('M - MEDIA   ')
print('G - GRANDE  ')
print('==================================')
tamanho = input('[P,M,G]: ').upper()
print('')
print('==================================')
print('         ESCOLHA A BEBIDA         ')
print('----------------------------------')
print('[1] COCA-COLA ')
print('[2] DOLLY     ')
print('[3] FANTA     ')
print('[4] GUARANÁ   ')
print('==================================')
bebida = int(input('ESCOLHA O NÚMERO DA BEBIDA: '))
print('==================================')
print('')
p = 20.00
m = 30.00
g = 40.00
coca = 10.00
fanta = 8.00
dolly = 4.00
guarana = 9.00

#INICIO PIZZA CALABRESA
if pizza == (1) and tamanho == ('P') and bebida == (1):
    total = ('CALABRESA PEQUENA E 1 COCA')
    valor = (p + coca)
elif pizza == (1) and tamanho == ('M') and bebida == (1):
    total = ('CALABRESA MEDIA E 1 COCA')
    valor = (m + coca)
elif pizza == (1) and tamanho == ('G') and bebida == (1):
    total = ('CALABRESA GRANDE E 1 COCA')
    valor = (g + coca)

elif pizza == (1) and tamanho == ('P') and bebida == (2):
    total = ('CALABRESA PEQUENA E 1 DOLLY')
    valor = (p + dolly)
elif pizza == (1) and tamanho == ('M') and bebida == (2):
    total = ('CALABRESA MEDIA E 1 DOLLY')
    valor = (m + dolly)
elif pizza == (1) and tamanho == ('G') and bebida == (2):
    total = ('CALABRESA GRANDE E 1 DOLLY')
    valor = (g + dolly)

elif pizza == (1) and tamanho == ('P') and bebida == (3):
    total = ('CALABRESA PEQUENA E 1 FANTA')
    valor = (p + fanta)
elif pizza == (1) and tamanho == ('M') and bebida == (3):
    total = ('CALABRESA MEDIA E 1 FANTA')
    valor = (m + fanta)
elif pizza == (1) and tamanho == ('G') and bebida == (3):
    total = ('CALABRESA GRANDE E 1 FANTA')
    valor = (g + fanta)

elif pizza == (1) and tamanho == ('P') and bebida == (4):
    total = ('CALABRESA PEQUENA E 1 GUARANÁ')
    valor = (p + guarana)
elif pizza == (1) and tamanho == ('M') and bebida == (4):
    total = ('CALABRESA MEDIA E 1 GUARANÁ')
    valor = (m + guarana)
elif pizza == (1) and tamanho == ('G') and bebida == (4):
    total = ('CALABRESA GRANDE E 1 GUARANÁ')
    valor = (g + guarana)
    
#FINAL DA PIZZA DE CALABRESA
#-------------------------------------------------------------------------------------
#COMEÇO DA PIZZA A MODA

elif pizza == (2) and tamanho == ('P') and bebida == (1):
    total = ('MODA PEQUENA E 1 COCA')
    valor = (p + coca)
elif pizza == (2) and tamanho == ('M') and bebida == (1):
    total = ('MODA MEDIA E 1 COCA')
    valor = (m + coca)
elif pizza == (2) and tamanho == ('G') and bebida == (1):
    total = ('MODA GRANDE E 1 COCA')
    valor = (g + coca)
    
elif pizza == (2) and tamanho == ('P') and bebida == (2):
    total = ('MODA PEQUENA E 1 DOLLY')
    valor = (p + dolly)
elif pizza == (2) and tamanho == ('M') and bebida == (2):
    total = ('MODA MEDIA E 1 DOLLY')
    valor = (m + dolly)
elif pizza == (2) and tamanho == ('G') and bebida == (2):
    total = ('MODA GRANDE E 1 DOLLY')
    valor = (g + dolly)
    
elif pizza == (2) and tamanho == ('P') and bebida == (3):
    total = ('MODA PEQUENA E 1 FANTA')
    valor = (p + fanta)
elif pizza == (2) and tamanho == ('M') and bebida == (3):
    total = ('MODA MEDIA E 1 FANTA')
    valor = (m + fanta)
elif pizza == (2) and tamanho == ('G') and bebida == (3):
    total = ('MODA GRANDE E 1 FANTA')
    valor = (g + fanta)

elif pizza == (2) and tamanho == ('P') and bebida == (4):
    total = ('MODA PEQUENA E 1 GUARANA')
    valor = (p + guarana)
elif pizza == (2) and tamanho == ('M') and bebida == (4):
    total = ('MODA MEDIA E 1 GUARANA')
    valor = (m + guarana)
elif pizza == (2) and tamanho == ('G') and bebida == (4):
    total = ('MODA GRANDE E 1 GUARANA')
    valor = (g + guarana)

#FINAL DA PIZZA A MODA 
#-----------------------------------------------------------------------------------
#COMEÇO DA PIZZA 4 QUEIJOS

elif pizza == (3) and tamanho == ('P') and bebida == (1):
    total = ('4 QUATRO QUEIJOS PEQUENA E 1 COCA')
    valor = (p + coca)
elif pizza == (3) and tamanho == ('M') and bebida == (1):
    total = ('4 QUATRO QUEIJOS MEDIA E 1 COCA')
    valor = (m + coca)
elif pizza == (3) and tamanho == ('G') and bebida == (1):
    total = ('4 QUATRO QUEIJOS GRANDE E 1 COCA')
    valor = (g + coca)
    
elif pizza == (3) and tamanho == ('P') and bebida == (2):
    total = ('4 QUATRO QUEIJOS PEQUENA E 1 DOLLY')
    valor = (p + dolly)
elif pizza == (3) and tamanho == ('M') and bebida == (2):
    total = ('4 QUATRO QUEIJOS MEDIA E 1 DOLLY')
    valor = (m + dolly)
elif pizza == (3) and tamanho == ('G') and bebida == (2):
    total = ('4 QUATRO QUEIJOS GRANDE E 1 DOLLY')
    valor = (g + dolly)
    
elif pizza == (3) and tamanho == ('P') and bebida == (3):
    total = ('4 QUATRO QUEIJOS PEQUENA E 1 FANTA')
    valor = (p + fanta)
elif pizza == (3) and tamanho == ('M') and bebida == (3):
    total = ('4 QUATRO QUEIJOS MEDIA E 1 FANTA')
    valor = (m + fanta)
elif pizza == (3) and tamanho == ('G') and bebida == (3):
    total = ('4 QUATRO QUEIJOS GRANDE E 1 FANTA')
    valor = (g + fanta)

elif pizza == (3) and tamanho == ('P') and bebida == (4):
    total = ('4 QUATRO QUEIJOS PEQUENA E 1 GUARANA')
    valor = (p + guarana)
elif pizza == (3) and tamanho == ('M') and bebida == (4):
    total = ('4 QUATRO QUEIJOS MEDIA E 1 GUARANA')
    valor = (m + guarana)
elif pizza == (3) and tamanho == ('G') and bebida == (4):
    total = ('4 QUATRO QUEIJOS GRANDE E 1 GUARANA')
    valor = (g + guarana)
    
#final da pizza de 4 queijos
#-----------------------------------------------------------------------------------
#inicio da pizza portuguesa

elif pizza == (4) and tamanho == ('P') and bebida == (1):
    total = ('PORTUGUESA PEQUENA E 1 COCA')
    valor = (p + coca)
elif pizza == (4) and tamanho == ('M') and bebida == (1):
    total = ('PORTUGUESA MEDIA E 1 COCA')
    valor = (m + coca)
elif pizza == (4) and tamanho == ('G') and bebida == (1):
    total = ('PORTUGUESA GRANDE E 1 COCA')
    valor = (g + coca)
    
elif pizza == (4) and tamanho == ('P') and bebida == (2):
    total = ('PORTUGUESA PEQUENA E 1 DOLLY')
    valor = (p + dolly)
elif pizza == (4) and tamanho == ('M') and bebida == (2):
    total = ('PORTUGUESA MEDIA E 1 DOLLY')
    valor = (m + dolly)
elif pizza == (4) and tamanho == ('G') and bebida == (2):
    total = ('PORTUGUESA GRANDE E 1 DOLLY')
    valor = (g + dolly)
    
elif pizza == (4) and tamanho == ('P') and bebida == (3):
    total = ('PORTUGUESA PEQUENA E 1 FANTA')
    valor = (p + fanta)
elif pizza == (4) and tamanho == ('M') and bebida == (3):
    total = ('PORTUGUESA MEDIA E 1 FANTA')
    valor = (m + fanta)
elif pizza == (4) and tamanho == ('G') and bebida == (3):
    total = ('PORTUGUESA GRANDE E 1 FANTA')
    valor = (g + fanta)

elif pizza == (4) and tamanho == ('P') and bebida == (4):
    total = ('PORTUGUESA PEQUENA E 1 GUARANA')
    valor = (p + guarana)
elif pizza == (4) and tamanho == ('M') and bebida == (4):
    total = ('PORTUGUESA MEDIA E 1 GUARANA')
    valor = (m + guarana)
elif pizza == (4) and tamanho == ('G') and bebida == (4):
    total = ('PORTUGUESA GRANDE E 1 GUARANA')
    valor = (g + guarana)
    
#final pizza portuguesa
#-----------------------------------------------------------------------  
if pizza in  (1, 2, 3, 4) and tamanho in ('P', 'M', 'G') and bebida in (1, 2, 3, 4):
    print('--------------------------------------------')
    print(f'seu pedido foi uma pizza {total}')
    print(f'o valor a pagar é de R$ {valor:.2f}')
    print('OBRIGADO PELA PREFERENCIA, E VOLTE SEMPRE :)')
    print('--------------------------------------------') 
    
else :
    print('OPS... PARECE QUE ALGO DEU ERRADO, TENTE NOVAMENTE :/')

    

    