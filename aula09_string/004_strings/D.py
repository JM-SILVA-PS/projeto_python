import os 
os.system('cls')

frase= 'albion online'
print(f'{frase}')

minuscula= frase.lower()
print(f'{minuscula}')

maiuscula= frase.upper()
print(f'{maiuscula}')

quantidade_de_caracteres = len(frase)
print(f'{frase} contem {quantidade_de_caracteres} caracteres')

segunda_palavra = frase[:-6]

print(f'a segunda palavra possui {segunda_palavra}')