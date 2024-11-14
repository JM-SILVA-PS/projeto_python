#Faça um programa que imprima os números no intervalo entre 1 e 10 em ordem inversa.

import os

os.system('cls')

for a in range (10 ,0,-1):
    print(f'{a}', end="|")