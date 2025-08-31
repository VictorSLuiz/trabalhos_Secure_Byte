def boletim() :
    print('\n' * 40) 
    print('--- BOLETIM ESCOLAR ---')
    name = input('DIGITE O NOME DO ALUNO : ')
    print('')
    print('-----------------------')
    print('')
    print('DIGTE A DISCIPLINA :')
    disc = input()
    print('')
    print('-----------------------')
    print('')
    nota = float(input(f'DIGITE A NOTA DE {name} : '))
    if nota < 6 :
        resultado = ('REPROVADO')
    elif nota == 6 :
        resultado = ('RECUPERAÇÃO')
    elif nota >= 7 and nota <= 9 :
        resultado = ('APROVADO ')
    elif nota >= 10 :
        resultado = ('APROVADO COM EXELÊNCIA')
    print('')
    print('-----------------------')
    print('')
    print('---- RESULTADOS ----')
    print(f'NOME : {name}')
    print(f'DISCIPLINA : {disc}')
    print(f'CONDIÇÃO : {resultado} ')
    print('-----------------------')
    print('')

while True :
    print(boletim())
    resp = input('CONTINUAR? [s/n] : ').upper()
    if resp != 'S' :
        break