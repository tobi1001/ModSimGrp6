import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

# Función de tendencia
def tendencia(x):
    return np.where(x < 0, 0, 
                    np.where(x <= 2, (x**3)/4, 0))


def generador(n):
    for i in range (n):
        u = np.random.uniform(0, 1)
        yield 2*np.power(u, 1/4)


# Número de muestras aleatorias
x = list(generador(100000))

# Graficar el histograma de los números generados
plt.figure(figsize=(10, 6))
plt.hist(x, bins=100, density=True, edgecolor='black', alpha=0.7)

# Graficar la función de densidad teórica
x_teoria = np.linspace(0, 2, 1000)
y_teoria = tendencia(x_teoria)
plt.plot(x_teoria, y_teoria, 'r-', linewidth=2, label='Función de densidad teórica')

plt.xlabel('x')
plt.ylabel('Densidad')
plt.title('Generador de variables aleatorias')
plt.legend()
plt.grid(True)
plt.show()