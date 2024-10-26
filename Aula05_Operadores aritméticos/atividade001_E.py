# E) Faça um programa que receba um número inteiro e exiba seu sucessor e antecessor. 
# IMPORTANDO BIBLIOTEA
import os

# LIMPANDO TERMINAL
os.system('cls')

# ENTRADA 
n1 = int(input('Coloque qualquer número: '))

# PROCESSO
sucessor = n1 + 1
antecessor = n1 - 1

# SAÍDA 
print(f'O sucessor de {n1} será {sucessor} e seu antecessor será {antecessor}')
