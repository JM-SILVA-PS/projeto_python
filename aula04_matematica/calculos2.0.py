import os
os.system('cls')

print('-'*70)
print('Operadores Artméticos: Ordem de Precedência')
print('-'*70)

nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))
nota3 = float(input('3ª nota: '))
nota4 = float(input('4ª nota: '))

soma = nota1 + nota2 + nota3 + nota4
media = nota1 + nota2 + nota3 + nota4 / 4
media_correta = (nota1 + nota2 + nota3 + nota4) / 4

print('---- Notas ----------')
print(f'Nota 1 : {nota1} | Nota 2: {nota2} |'
      f'Nota 3: {nota1} | nota 4: {nota4}')
print('-'*70)
print(f'Média errada: {media}')
print(f'Média correta: {media_correta}')
print('-'*70)
