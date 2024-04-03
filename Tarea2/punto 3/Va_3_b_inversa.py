import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

# Función de densidad
def funcion_densidad(x, a):
    return np.where(x <= 0, 0,
                    np.where(x <= a, x / (a * (1 - a)),
                             np.where(x <= 1 - a, 1 / (1 - a),
                                      np.where(x <= 1, (1 - x) / (a * (1 - a)), 0))))

# Función de distribución acumulada
def funcion_acumulada(x, a):
    return np.where(x < 0, 0,
                    np.where(x <= a/(2*(1-a)), x**2 / (2 * a * (1 - a)),
                             np.where(x <= (3*a - 2)/(2*a - 2), (-a + 2*x)/(2*(-a + 1)))),
                                      np.where(x <= 1, (-x**2 - 1 + 2*x)/(2*a * (-a + 1)), 1))

# Transformada inversa
def transformada_inversa(a, n):
    variables_aleatorias = []
    while len(variables_aleatorias) < n:
        u = np.random.uniform(0, 1)
        if u < 0: 
            variables_aleatorias.append(0)
        elif u <= (a/(2*(1-a))):
            variables_aleatorias.append(np.sqrt(2 * a * u * (1 - a)))
        elif u <= (3*a - 2)/(2*a - 2):
            variables_aleatorias.append(-a*u + u + a/2) 
        elif u <= 1:
            variables_aleatorias.append(1 - np.sqrt(2 * a * (a-1) * (u-1)))

    return variables_aleatorias


a = 0.44
x = transformada_inversa(a, 100000) # Número de muestras aleatorias

# Graficar el histograma de los números generados
plt.figure(figsize=(10, 6))
plt.hist(x, bins=100, density=True, edgecolor='black', alpha=0.7)

# Graficar la función de densidad teórica
x_teoria = np.linspace(0, 1, 1000)
y_teoria = funcion_densidad(x_teoria, a)
plt.plot(x_teoria, y_teoria, 'r-', linewidth=2, label='Función de densidad teórica')

plt.xlabel('x')
plt.ylabel('Densidad')
plt.title('Método de la Transformada inversa (b) con a = {}'.format(a))
plt.legend()
plt.grid(True)
plt.show()