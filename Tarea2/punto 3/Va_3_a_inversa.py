import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)

# Función de densidad
def funcion_densidad(x):
    return np.where(x < -1, 0, 
                    np.where(x > 1, 0, (3*(x**2)/2)))

# Función de distribución acumulada
def funcion_acumulada(x):
    return np.where(x < -1, 0, 
                    np.where(x > 1, 1, ((x**3 + 1)/ 2)))

# Transformada inversa
def transformada_inversa(n):
    variables_aleatorias = []

    while len(variables_aleatorias) < n:
        u = np.random.uniform(0, 1)
        
        if u < 0:
            variables_aleatorias.append(-1) 
        elif u <= 1:
            variables_aleatorias.append(np.cbrt(2*u - 1))
        else:
            variables_aleatorias.append(1)
    return variables_aleatorias

# Número de muestras aleatorias
x = transformada_inversa(100000) 

# Graficar el histograma de los números generados
plt.figure(figsize=(10, 6))
plt.hist(x, bins=100, density=True, edgecolor='black', alpha=0.7)

# Graficar la función de densidad teórica
x_teoria = np.linspace(-1, 1, 1000)
y_teoria = funcion_densidad(x_teoria)
plt.plot(x_teoria, y_teoria, 'r-', linewidth=2, label='Función de densidad teórica')

plt.xlabel('x')
plt.ylabel('Densidad')
plt.title('Método de la Transformada inversa (a)')
plt.legend()
plt.grid(True)
plt.show()