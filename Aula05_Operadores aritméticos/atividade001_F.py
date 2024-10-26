# Desenvolva um programa que peça um número qualquer e calcule o dobro e o triplo desse número.
 # IMPORTANDO BIBLIOTEA
import os

# LIMPANDO TERMINAL
os.system('cls')

# ENTRADA 
numero = float(input('Escolha qualquer valor: '))

# PROCESSAMENTO 
dobro = (numero) * 2
triplo = (numero) * 3

# SAÍDA 
(print(f'Com o {numero} seu dobro será {dobro} e seu triplo será {triplo}'))
