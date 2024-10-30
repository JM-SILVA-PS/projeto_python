# importando biblioteca
import os

# limpando terminal
os.system('cls')

# entrada
a = str(input('insira o primeiro numero:'))
b = str(input('insira o segundo numero:'))
c = str(input('insira o terceiro numero:'))
resposta = ''

if a > b > c:
    resposta1 = f'{a} é maior que {b} e {c}'

elif b > c:
    resposta1 = f'{b} é maior que {a} e {c}'


else:
    resposta1 = f'{c} é maior que {a} e {b}'

print(resposta1)

if a < b < c:
    resposta2 = f'{a} é menor que {b} e {c}'
elif b < c:
    resposta2 = f'{b} é menor que {a} e {c}'
else:
    resposta2 = f'{c} é menor que {a} e {b}'

    print(resposta2)

if a == b == c:
    resposta3 = f'os três numeros são iguais'
else:
    resposta3 = f' os numeros não são todos iguais'
print(resposta3)
