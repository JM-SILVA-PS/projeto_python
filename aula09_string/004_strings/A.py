import os 
os.system('cls')

nome = input('Seu nome: ')
nome_do_meio = input('Seu nome do meio: ')
sobrenome = input('Seu sobrenome: ')

nome_completo = nome + ' ' + nome_do_meio + ' ' + sobrenome
print(f'ola {nome_completo}')