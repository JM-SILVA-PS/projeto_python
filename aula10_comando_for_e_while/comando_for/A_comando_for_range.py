import os 

os.system('cls')

print('Estrutura de controle for range')

print()

for var_iteradora in range(1,7):
    print(f'valor: {var_iteradora}', end = '|')

    print()
    print()

    inicio = 1

    fim = 30

    passo = 3

    for var_iteradora in range(inicio, fim, passo):
        print(f'Valor:{var_iteradora}', end = '|')

    print()
    print()