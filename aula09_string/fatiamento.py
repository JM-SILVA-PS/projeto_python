import os 
os.system('cls')

frase = 'String em python!'

print(f'String original: {frase}')

primeiros_cinco = frase[:5]
print(f'Primeiros cinco caracteres: {primeiros_cinco}')

ultimos_dez = frase[-10:]
print(f'ultimos dez caracteres:{ultimos_dez}')

quarto_ao_decimo = frase[3:10]
print(f'Do quarto ao decimo caractere: {quarto_ao_decimo}')

a_cada_dois = frase[::2]
print(f'A cada dois caracteres: {a_cada_dois}')

invertida = frase[::-1]
print(f'string invertida: {invertida}')