import os

os.system('cls')

print('Estrutura de controle while else break')

print()

while (True):

    nome = str(input('Digite um nome [s - Sair]: ')).lower()
    
    if (nome != 's'):
        print('Continua digitando...')
    else:
        print('Você digitou "s" para sair!!!')

        break

    print()