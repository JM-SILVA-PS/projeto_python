import random
import os

os.system('cls')

print('Numero aleatorio')
numero_aleatorio = random.random()
print(f'O numero gerado foi : { numero_aleatorio}')
print('Numero aleatorio decimal no intervalo')
aleatorio_inteiro = random.randint(1,20)
print(f'O numero inteiro gerado foi: {aleatorio_inteiro}')

print('Numero aleatorio decimal no intervalo')
aleatorio_decimal = random.uniform(1,10)
print(f'O numero decimal gerado foi:{aleatorio_decimal}')

print('Sorteio em um lista')
lista = ['agata','coly','isis','bia']
nome_sorteado = random.choice(lista)
print(f'Lista:{lista}')
print(f'O nome escolhido foi : {nome_sorteado}')

print('Embaralhar sequencia')
lista2 = ['agata','coly','isis','bia']
print(f'Lista antiga: {lista2}')

random.shuffle(lista2)
print(f'Lista nova:{lista2}')
print('.'*70)

print('Retorno de elementos unicos de uma população')
numeros = [1,2,3,4,5,6,7]
amostra_aleaoria = random.sample(numeros, 5)
print(f'Retorno da amostragem: { amostra_aleaoria}')
print('.'*70)
