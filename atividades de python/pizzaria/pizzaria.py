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
print('==================================')
print('         ESCOLHA O TAMANHO        ')
print('----------------------------------')
print('P - PEQUENA ')
print('M - MEDIA   ')
print('G - GRANDE  ')
print('==================================')
tamanho = input('[P,M,G]: ').isupper()
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

#INICIO PIZZA CALABRESA
if pizza == (1) and tamanho == ('P') and bebida == (1):
    print('SEU PEDIDO FOI UMA PIZZA PEQUENA, SABOR CALABRESA, E UMA COCA-COLA ')
    print('TOTAL A PAGAR: R$ 30,00')
elif pizza == (1) and tamanho == ('M') and bebida == (1):
    print('SEU PEDIDO FOI UMA PIZZA MEDIA, SABOR CALABRESA, E UMA COCA-COLA ')
    print('TOTAL A PAGAR: R$ 40,00')
elif pizza == (1) and tamanho == ('G') and bebida == (1):
    print('SEU PEDIDO FOI UMA PIZZA GRANDE, SABOR CALABRESA, E UMA COCA-COLA ')
    print('TOTAL A PAGAR: R$ 50,00')

elif pizza == (1) and tamanho == ('P') and bebida == (2):
    print('SEU PEDIDO FOI UMA PIZZA PEQUENA, SABOR CALABRESA, E UM DOLLY ')
    print('TOTAL A PAGAR: R$ 24,00')
elif pizza == (1) and tamanho == ('M') and bebida == (2):
    print('SEU PEDIDO FOI UMA PIZZA MEDIA, SABOR CALABRESA, E UM DOLLY ')
    print('TOTAL A PAGAR: R$ 34,00')
elif pizza == (1) and tamanho == ('G') and bebida == (2):
    print('SEU PEDIDO FOI UMA PIZZA GRANDE, SABOR CALABRESA, E UM DOLLY ')
    print('TOTAL A PAGAR: R$ 44,00')

elif pizza == (1) and tamanho == ('P') and bebida == (3):
    print('SEU PEDIDO FOI UMA PIZZA PEQUENA, SABOR CALABRESA, E UMA FANTA ')
    print('TOTAL A PAGAR: R$ 28,00')
elif pizza == (1) and tamanho == ('M') and bebida == (3):
    print('SEU PEDIDO FOI UMA PIZZA MEDIA, SABOR CALABRESA, E UMA FANTA ')
    print('TOTAL A PAGAR: R$ 38,00')
elif pizza == (1) and tamanho == ('G') and bebida == (3):
    print('SEU PEDIDO FOI UMA PIZZA GRANDE, SABOR CALABRESA, E UMA FANTA ')
    print('TOTAL A PAGAR: R$ 48,00')

elif pizza == (1) and tamanho == ('P') and bebida == (4):
    print('SEU PEDIDO FOI UMA PIZZA PEQUENA, SABOR CALABRESA, E UM GUARANÁ ')
    print('TOTAL A PAGAR: R$ 29,00')
elif pizza == (1) and tamanho == ('M') and bebida == (4):
    print('SEU PEDIDO FOI UMA PIZZA MEDIA, SABOR CALABRESA, E UM GUARANÁ ')
    print('TOTAL A PAGAR: R$ 39,00')
elif pizza == (1) and tamanho == ('G') and bebida == (4):
    print('SEU PEDIDO FOI UMA PIZZA GRANDE, SABOR CALABRESA, E UM GUARANÁ ')
    print('TOTAL A PAGAR: R$ 49,00')
#FINAL DA PIZZA DE CALABRESA
#-------------------------------------------------------------------------------------
#COMEÇO DA PIZZA A MODA
elif pizza == (2) and tamanho == ('P') and bebida == (1):
    print('SEU PEDIDO FOI UMA PIZZA PEQUENA, SABOR A MODA, E UMA COCA-COLA ')
    print('TOTAL A PAGAR: R$ 30,00')
elif pizza == (2) and tamanho == ('M') and bebida == (1):
    print('SEU PEDIDO FOI UMA PIZZA MEDIA, SABOR A MODA, E UMA COCA-COLA ')
    print('TOTAL A PAGAR: R$ 40,00')
elif pizza == (2) and tamanho == ('G') and bebida == (1):
    print('SEU PEDIDO FOI UMA PIZZA GRANDE, SABOR A MODA, E UMA COCA-COLA ')
    print('TOTAL A PAGAR: R$ 50,00')
    
elif pizza == (2) and tamanho == ('P') and bebida == (2):
    print('SEU PEDIDO FOI UMA PIZZA PEQUENA, SABOR A MODA, E UM DOLLY ')
    print('TOTAL A PAGAR: R$ 34,00')
elif pizza == (2) and tamanho == ('M') and bebida == (2):
    print('SEU PEDIDO FOI UMA PIZZA MEDIA, SABOR A MODA, E UM DOLLY ')
    print('TOTAL A PAGAR: R$ 44,00')
elif pizza == (2) and tamanho == ('G') and bebida == (2):
    print('SEU PEDIDO FOI UMA PIZZA GRANDE, SABOR A MODA, E UM DOLLY ')
    print('TOTAL A PAGAR: R$ 54,00')
    
elif pizza == (2) and tamanho == ('P') and bebida == (3):
    print('SEU PEDIDO FOI UMA PIZZA PEQUENA, SABOR A MODA, E UMA FANTA  ')
    print('TOTAL A PAGAR: R$ 38,00')
elif pizza == (2) and tamanho == ('M') and bebida == (3):
    print('SEU PEDIDO FOI UMA PIZZA MEDIA, SABOR A MODA, E UMA FANTA ')
    print('TOTAL A PAGAR: R$ 48,00')
elif pizza == (2) and tamanho == ('G') and bebida == (3):
    print('SEU PEDIDO FOI UMA PIZZA GRANDE, SABOR A MODA, E UMA FANTA ')
    print('TOTAL A PAGAR: R$ 58,00')

elif pizza == (2) and tamanho == ('P') and bebida == (4):
    print('SEU PEDIDO FOI UMA PIZZA PEQUENA, SABOR A MODA, E UM GUARANÁ ')
    print('TOTAL A PAGAR: R$ 29,00')
elif pizza == (2) and tamanho == ('M') and bebida == (4):
    print('SEU PEDIDO FOI UMA PIZZA MEDIA, SABOR A MODA, E UM GUARANÁ ')
    print('TOTAL A PAGAR: R$ 39,00')
elif pizza == (2) and tamanho == ('G') and bebida == (4):
    print('SEU PEDIDO FOI UMA PIZZA GRANDE, SABOR A MODA, E UM GUARANÁ ')
    print('TOTAL A PAGAR: R$ 49,00')
#FINAL DA PIZZA A MODA 
#-----------------------------------------------------------------------------------
#COMEÇO DA PIZZA 4 QUEIJOS

elif pizza == (3) and tamanho == ('P') and bebida == (1):
    print('SEU PEDIDO FOI UMA PIZZA PEQUENA, SABOR 4 QUEIJOS, E UMA COCA-COLA ')
    print('TOTAL A PAGAR: R$ 30,00')
elif pizza == (3) and tamanho == ('M') and bebida == (1):
    print('SEU PEDIDO FOI UMA PIZZA MEDIA, SABOR 4 QUEIJOS, E UMA COCA-COLA ')
    print('TOTAL A PAGAR: R$ 40,00')
elif pizza == (3) and tamanho == ('G') and bebida == (1):
    print('SEU PEDIDO FOI UMA PIZZA GRANDE, SABOR 4 QUEIJOS, E UMA COCA-COLA ')
    print('TOTAL A PAGAR: R$ 50,00')
    
elif pizza == (3) and tamanho == ('P') and bebida == (2):
    print('SEU PEDIDO FOI UMA PIZZA PEQUENA, SABOR 4 QUEIJOS, E UM DOLLY ')
    print('TOTAL A PAGAR: R$ 34,00')
elif pizza == (3) and tamanho == ('M') and bebida == (2):
    print('SEU PEDIDO FOI UMA PIZZA MEDIA, SABOR 4 QUEIJOS, E UM DOLLY ')
    print('TOTAL A PAGAR: R$ 44,00')
elif pizza == (3) and tamanho == ('G') and bebida == (2):
    print('SEU PEDIDO FOI UMA PIZZA GRANDE, SABOR 4 QUEIJOS, E UM DOLLY ')
    print('TOTAL A PAGAR: R$ 54,00')
    
elif pizza == (3) and tamanho == ('P') and bebida == (3):
    print('SEU PEDIDO FOI UMA PIZZA PEQUENA, SABOR 4 QUEIJOS, E UMA FANTA  ')
    print('TOTAL A PAGAR: R$ 38,00')
elif pizza == (3) and tamanho == ('M') and bebida == (3):
    print('SEU PEDIDO FOI UMA PIZZA MEDIA, SABOR 4 QUEIJOS, E UMA FANTA ')
    print('TOTAL A PAGAR: R$ 48,00')
elif pizza == (3) and tamanho == ('G') and bebida == (3):
    print('SEU PEDIDO FOI UMA PIZZA GRANDE, SABOR 4 QUEIJOS, E UMA FANTA ')
    print('TOTAL A PAGAR: R$ 58,00')

elif pizza == (3) and tamanho == ('P') and bebida == (4):
    print('SEU PEDIDO FOI UMA PIZZA PEQUENA, SABOR 4 QUEIJOS, E UM GUARANÁ ')
    print('TOTAL A PAGAR: R$ 29,00')
elif pizza == (3) and tamanho == ('M') and bebida == (4):
    print('SEU PEDIDO FOI UMA PIZZA MEDIA, SABOR 4 QUEIJOS, E UM GUARANÁ ')
    print('TOTAL A PAGAR: R$ 39,00')
elif pizza == (3) and tamanho == ('G') and bebida == (4):
    print('SEU PEDIDO FOI UMA PIZZA GRANDE, SABOR 4QUEIJOS, E UM GUARANÁ ')
    print('TOTAL A PAGAR: R$ 49,00')
    
#-----------------------------------------------------------------------------------

elif pizza == (4) and tamanho == ('P') and bebida == (1):
    print('SEU PEDIDO FOI UMA PIZZA PEQUENA, SABOR PORTUGUESA, E UMA COCA-COLA ')
    print('TOTAL A PAGAR: R$ 30,00')
elif pizza == (4) and tamanho == ('M') and bebida == (1):
    print('SEU PEDIDO FOI UMA PIZZA MEDIA, SABOR PORTUGUESA, E UMA COCA-COLA ')
    print('TOTAL A PAGAR: R$ 40,00')
elif pizza == (4) and tamanho == ('G') and bebida == (1):
    print('SEU PEDIDO FOI UMA PIZZA GRANDE, SABOR PORTUGUESA, E UMA COCA-COLA ')
    print('TOTAL A PAGAR: R$ 50,00')
    
elif pizza == (4) and tamanho == ('P') and bebida == (2):
    print('SEU PEDIDO FOI UMA PIZZA PEQUENA, SABOR PORTUGUESA, E UM DOLLY ')
    print('TOTAL A PAGAR: R$ 34,00')
elif pizza == (4) and tamanho == ('M') and bebida == (2):
    print('SEU PEDIDO FOI UMA PIZZA MEDIA, SABOR PORTUGUESA, E UM DOLLY ')
    print('TOTAL A PAGAR: R$ 44,00')
elif pizza == (4) and tamanho == ('G') and bebida == (2):
    print('SEU PEDIDO FOI UMA PIZZA GRANDE, SABOR PORTUGUESA, E UM DOLLY ')
    print('TOTAL A PAGAR: R$ 54,00')
    
elif pizza == (4) and tamanho == ('P') and bebida == (3):
    print('SEU PEDIDO FOI UMA PIZZA PEQUENA, SABOR PORTUGUESA, E UMA FANTA  ')
    print('TOTAL A PAGAR: R$ 38,00')
elif pizza == (4) and tamanho == ('M') and bebida == (3):
    print('SEU PEDIDO FOI UMA PIZZA MEDIA, SABOR PORTUGUESA, E UMA FANTA ')
    print('TOTAL A PAGAR: R$ 48,00')
elif pizza == (4) and tamanho == ('G') and bebida == (3):
    print('SEU PEDIDO FOI UMA PIZZA GRANDE, SABOR PORTUGUESA, E UMA FANTA ')
    print('TOTAL A PAGAR: R$ 58,00')

elif pizza == (4) and tamanho == ('P') and bebida == (4):
    print('SEU PEDIDO FOI UMA PIZZA PEQUENA, SABOR PORTUGUESA, E UM GUARANÁ ')
    print('TOTAL A PAGAR: R$ 29,00')
elif pizza == (4) and tamanho == ('M') and bebida == (4):
    print('SEU PEDIDO FOI UMA PIZZA MEDIA, SABOR PORTUGUESA, E UM GUARANÁ ')
    print('TOTAL A PAGAR: R$ 39,00')
elif pizza == (4) and tamanho == ('G') and bebida == (4):
    print('SEU PEDIDO FOI UMA PIZZA GRANDE, SABOR PORTUGUESA, E UM GUARANÁ ')
    print('TOTAL A PAGAR: R$ 49,00')
elif pizza != (1,2,3,4) or tamanho != ('P,M,G') or bebida != (1,2,3,4) :
    print('ERRROR, tente novamente!!')
