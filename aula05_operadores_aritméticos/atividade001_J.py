#J) Elabore um programa que peça as dimensões de um retângulo e calcule seu perímetro.

#importando bibliotecas
import os

#limpar o terminal
os.system('cls')

#Entrada

base = float(input('qual é a base do retangulo?'))
altura = float(input('qual é a altura do retangulo?'))

#Processamento 
perimetro = 2 * (base + altura)

#Saída
print(f'O perimetro do retangulo é: {perimetro}')