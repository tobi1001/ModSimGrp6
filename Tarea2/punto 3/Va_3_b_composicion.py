import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

# Función de densidad
def funcion_densidad(x, a):
    return np.where(x <= 0, 0,
                    np.where(x <= a, x / (a * (1 - a)),
                             np.where(x <= 1 - a, 1 / (1 - a),
                                      np.where(x <= 1, (1 - x) / (a * (1 - a)), 0))))

def composicion(a, n):
    variables_aleatorias = []

    while len(variables_aleatorias) < n:
        u1 = np.random.uniform(0, 1)
        u2 = np.random.uniform(0, 1)

        if u1 <= a/(2*(1-a)):
            variables_aleatorias.append(a*np.sqrt(u2))
        elif u1 <= (2-3*a)/(2*(1-a)):
            variables_aleatorias.append((1-2*a)*u2 + a)
        else:
            variables_aleatorias.append(1 - a*np.sqrt(1-u2))
    
    return variables_aleatorias

a = 0.44
x = composicion(a, 100000)

# Graficar el histograma de los números generados
plt.figure(figsize=(10, 6))
plt.hist(x, bins=100, density=True, edgecolor='black', alpha=0.7)

# Graficar la función de densidad teórica
x_teoria = np.linspace(0, 1, 1000)
y_teoria = funcion_densidad(x_teoria, a)
plt.plot(x_teoria, y_teoria, 'r-', linewidth=2, label='Función de densidad teórica')

plt.xlabel('x')
plt.ylabel('Densidad')
plt.title('Método de composición (b) con a = {}'.format(a))
plt.legend()
plt.grid(True)
plt.show()