# Crie um programa que converta uma medida em metros para centímetros e milímetros.

# IMPORTANDO BIBLIOTECA

import os

# LIMPANDO TERMINAL

os.system('cls')

# ENTRADA 

metros = float(input('Insira a medida em metros \n que deseja converter: '))

# PROCESSAMENTO
centimetro = metros * 100
milimetro = metros * 1000

# SAÍDA  
print(f'Convertendo {metros} metro(s) para centímetros será {centimetro} e \n para milímetros será {milimetro}')