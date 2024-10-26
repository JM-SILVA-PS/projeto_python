# Desenvolva um programa que solicite um valor em reais e calcule quantos dólares podem ser comprados com esse valor.

# IMPORTANDO BIBLIOTECA 
import os

# LIMPANDO TERMINAL
os.system('cls')

# ENTRADA
reais = float(input('Insira o valor em reais: '))

# PROCESSAMENTO
dolar = reais * 5.71

#Saída
print(f'O valor {reais} real/reais será {dolar} dólar/dólares')