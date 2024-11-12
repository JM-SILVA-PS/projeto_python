#812
import os 

os.system('cls')

print('Estrutura de controle somatorio')

print()

soma = 0 

for var_iteradora in range(0,10):
    numero = int(input(f'digite o {var_iteradora + 1}º numero:'))

    soma += numero


print(f'A soma dos numeros é: {soma}')