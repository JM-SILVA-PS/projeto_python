import os
os.system('cls')

texto = 'Ola, mundo'

print(f'texto:{texto}')
if 'mundo' in texto:
    print('a palavra "mundo" esta presente na string')
else:
    print('a palavra "mundo"não esta presente na string.')

texto2 = 'Ola, python'

print(f'texto:{texto2}')
if 'mundo'not in texto2:
        print('a palavra "mundo"não esta presente na string.')
else:
        print('a palavra "mundo"esta presente na string.')
