import os

os.system('cls')

print('-'*70)
print('Estudo de condicional:Part 1')
print('='*70)

numero = float(input('Digite um numero:'))
resposta = ''

if numero % 2 == 0:
    resposta = f'O número {numero} é par'
else:
    resposta = f'O número {numero} é impart'

print('='*70)
print(resposta)
print('PRAISE THE SUN!\n')