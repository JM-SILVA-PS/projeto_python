import os 
os.system('cls')

nome = input('escreva o seu nome: ')

separado = nome.split()

primeiro_nome =separado[0:1]
ultimo_nome = separado[-1:]

print(f'O primerio nome é {primeiro_nome} e o ultimo nome é {ultimo_nome}')