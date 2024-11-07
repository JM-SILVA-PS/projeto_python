import os 
os.system('cls')


frase = input('Escreva a frase:')

vogal_a = frase.count('a')
vogal_e = frase.count('e')
vogal_i =frase.count('i')
vogal_o = frase.count('o')
vogal_u =frase.count('u')
quantidade_de_vogais= vogal_a + vogal_e + vogal_i + vogal_o + vogal_u

print(f'As vogais aparecem {quantidade_de_vogais} vezes')
print(f'A vogal "A" aparece {vogal_a} vezes')
print(f'A vogal "E" aparece {vogal_e} vezes')
print(f'A vogal "I" aparece {vogal_i} vezes')
print(f'A vogal "O" aparece {vogal_o} vezes')
print(f'A vogal "U" aparece {vogal_u} vezes')