import os

os.system('cls')

print('Estrutura de controle com input e if')

print()

soma = 0

for var_iteradora in range(0,6):
    numero = int(input(f'{var_iteradora + 1}º numero:'))

    if (numero % 2 == 0):
        print(f'O numero {numero} é par')

    else:
        print(f'o numero {numero} é impar')

        print()