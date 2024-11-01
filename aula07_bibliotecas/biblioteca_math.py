import os
import math

os.system('cls')

print('-'*70)
print('estudo da biblioteca matematica math')
print('='*70)
print()

base = 2
expoente = 3
angulo = 30
radicando = 81
co = 5
ca = 10

potencia = math.pow(base, expoente)
raizQuadrada = math.sqrt(radicando)
seno = math.sin(math.radians(angulo))
cosseso = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
hipotenusa = math.hypot(co,ca)

print(f'{base} elevado a {expoente} é igual a : {potencia}')
print(F' A raiz quadrada de {radicando} é : {raizQuadrada}')
print(f'O seno de {angulo} é: {seno:.2f}')
print(f'O cosseno de {angulo} é: {cosseso:.2f}')
print(f'A tangente de {angulo} é: {tangente:.2f}')
print(f'O valor da hipotenusa é: {hipotenusa:.2f}')
print('-'*70)
