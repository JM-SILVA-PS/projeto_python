#Faça um programa que imprima os números pares entre 0 e 100.

import os

os.system('cls')

contador= 0

while (contador <=100):

    contador +=1

    if (contador %2 ==0):
        print(f'{contador}',end = "|")