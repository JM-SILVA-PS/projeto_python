# D) Implemente um programa que receba dois números e realize a divisão, formatando o resultado com quatro casas decimais.

# IMPORTANDO BIBLIOTEA
import os

# LIMPANDO TERMINAL
os.system('cls')

# ENTRADA
numero1 = float(input('Insira o 1° número: '))
numero2 = float(input('Insira o 2° número: '))

# PROCESSAMENTO
divisao = (numero1) / (numero2)

# SAÍDA 
float(input(f'A divisão de {numero1} e {numero2} será {divisao:.4f}'))
print('=')