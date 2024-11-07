import os 
os.system('cls')

aluno = input('insira o nome do aluno:').lower()

o = aluno.count('o')
print(f'o nome {aluno} possui {o} letras o')

primeira_vez= aluno.find('o')
print(f'a letra o aparece pela primeira vez em {primeira_vez}')

ultima_vez=aluno.rfind('o')
print(f'a letra o aparece pela ultima vez em {ultima_vez}')