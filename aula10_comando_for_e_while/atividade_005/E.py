#Faça um programa que some a quantidade de números pares encontrados no intervalo entre 0 e 100.

import os

os.system('cls')

contador= 0

for a in range (0 , 101):
    if ( a  %2 ==0):
        contador += a
        print(f'{contador}',end = "|")  