# C) Elabore um programa que receba quatro notas de um aluno e calcule a média dessas notas


# IMPORTANDO BIBLIOTEA
import os

# LIMPANDO TERMINAL
os.system('cls')

# ENTRADA
nota1 = float(input('1° nota: '))
nota2 = float(input('2° nota: '))
nota3 = float(input('3° nota: '))
nota4 = float(input('4° nota: '))

# PROCESSAMENTO
media = (nota1 + nota2 + nota3 + nota4) / 4

#SAÍDA 
print(f'A média das seguintes notas \n nota 1: {nota1}, nota 2: {nota2}, nota 3: {nota3} e nota 4: {nota4} será {media}')
