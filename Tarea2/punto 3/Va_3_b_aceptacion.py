import numpy as np
import matplotlib.pyplot as plt

def funcion_densidad(x, a):
    return np.where(x <= 0, 0, 
                    np.where(x <= a, x / (a * (1 - a)), 
                             np.where(x <= 1 - a, 1 / (1 - a), 
                                      np.where(x <= 1, (1 - x) / (a * (1 - a)), 0))))

def aceptacion_rechazo(a, n):
    variables_aleatorias = []
    while len(variables_aleatorias) < n:
        u1 = np.random.uniform(0, 1)
        u2 = np.random.uniform(0, 1)

        if u1 <= a:
            y = u1/a
        elif u1 <= 1 - a:
            y = 1
        else:
            y = (1-u1)/a

        if u2 <= y:
            variables_aleatorias.append(u1)


    return variables_aleatorias

a = 0.3
x = aceptacion_rechazo(a, 100000)

# Graficar el histograma de la muestra generada
plt.figure(figsize=(8, 4))
plt.hist(x, bins=100, density=True, alpha=0.7, edgecolor='black')
plt.xlabel('x')
plt.ylabel('Densidad')
plt.title('Método de aceptación y rechazo (b) con a = {}'.format(a))
plt.grid(True)

# Graficar la función de probabilidad
x = np.linspace(0, 1, 100)
y = [funcion_densidad(xi, a) for xi in x]
plt.plot(x, y, 'r-', linewidth=2, label='Función de densidad teórica')
plt.legend()

plt.tight_layout()
plt.show()
