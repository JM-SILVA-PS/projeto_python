import os 
import math

os.system('cls')


angulo = float(input('entre com o angulo '))

seno = math.sin(math.radians(angulo))
cosseso = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'o seno de {angulo} é  {seno:.2f}')
print(f'O cosseso de {angulo} é {cosseso:.2f}')
print(f'O tangente de {angulo} é {tangente:.2f}')
