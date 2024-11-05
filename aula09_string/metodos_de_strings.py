import os

os.system('cls')

frase1 = 'ola,mundo!'
quantide_caracteres = len(frase1)
print(f'a frase {frase1} \ncontem {quantide_caracteres} caracteres')

minusculas = frase1.lower()
print(f'frase original:{frase1}')
print(f'frase nova:{minusculas}')

captalizada = frase1.capitalize()
print(f'frase original:{frase1}')
print(f'frase nova:{minusculas}')

frase2= 'ola mundo'
sem_espacos = frase2.strip()
print(f'frase original:{frase2}')
print(f'frase nova:{sem_espacos}')

substituicao = frase1.replace('mundo','python')
print(f'frase original : {frase1}')
print(f'frase nova: {substituicao}')

lista = frase1.split(',')
print(f'frase original:{frase1}')
print(f'frase nova:{lista}')

lista=['ola','mundo']
juncao= '-'.join(lista)
print(f'frase original:{lista}')
print(f'frase nova:{juncao}')
