#importando biblioteca
import os 

#limpando terminal
os.system('cls')

          
# Definindo os coeficientes da equação quadrática
a = 1
b = -6
c = 5

# Calculando o valor de delta (b² - 4ac)
b_squared = b * b         # b²
ac_term = 4 * a * c        # 4ac
delta = b_squared - ac_term # delta = b² - 4ac

# Calculando a raiz quadrada de delta manualmente
sqrt_delta = delta ** 0.5  # sqrt(delta)

# Calculando as duas raízes usando a fórmula de Bhaskara
x1 = (-b + sqrt_delta) / (2 * a)  # primeira raiz
x2 = (-b - sqrt_delta) / (2 * a)  # segunda raiz

# Exibindo os resultados
print("A primeira raiz (x1) é:", x1)
print("A segunda raiz (x2) é:", x2)
