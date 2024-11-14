#Crie um programa que realiza a contagem de 1 até 100, usando apenas de números ímpares, ao final do processo exiba na tela quantos números ímpares foram encontrados nesse intervalo, assim como a soma dos mesmos.

import os

os.system('cls')


contador= 0
quantidade = 0
for a in range (0 , 101):
    if ( a  %2 ==1):
        contador += a
        quantidade += 1
print(f'{contador}',end = "|")  
print(f'{quantidade}')