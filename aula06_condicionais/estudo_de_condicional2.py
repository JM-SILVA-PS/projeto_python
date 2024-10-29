import os

os.system('cls')

a = 10
b = 5
resposta = ''

print('-'*70)
print('Estudo de condicional (Simples)')
print('='*70)

if a > b:
    resposta = f'{a} é maior que {b}'
else:
    resposta = f'{a}não é maior que {b}'

print('-'*70)
print(resposta)

a = 5
b = 5

print('-'*70)
print('Estudo de condicional (aninhada)')
print('-'*70)

if a > b:
    resposta = f'{a} é maior que {b}'
elif a < b :
    resposta = f'{a} é menor que {b}'
else:
    resposta = f'O valores são iguais: {a} = {b}'

print('-'*70)
print(resposta)
print('-'*70)
print()