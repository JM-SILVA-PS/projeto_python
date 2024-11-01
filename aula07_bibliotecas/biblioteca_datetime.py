import os

from datetime import datetime
from datetime import date

os.system('cls')

data = datetime.now()

data_formatada = data.strftime('%d/%m/%Y')

data_hora_formatada = data.strftime('%d/%m/%Y %H:%M')

print(f'data formatada: {data_formatada}')
print(f'Data e hora formatadas: {data_hora_formatada}')

data_atual = date.today()
nascimento = 1970
idade = data_atual.year - nascimento

print('-'*70)
print(f'Data atual no sistema: {data_atual}')
print(f'Nascimento.............:{nascimento}')

print(f'Ano atual..............:{data_atual.year}')

print(f'Sua idade é...............:{idade} anos')
print('-'*70)

