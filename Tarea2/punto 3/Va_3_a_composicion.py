import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)

# Función de densidad
def funcion_densidad(x):
    return np.where(x < -1, 0, 
                    np.where(x <= 0, (1/2)*(3*x**2),
                            np.where(x <= 1, (1/2)*(3*x**2), 0)))

# Función de composición
def composicion(n):
    variables_aleatorias = []
    while len(variables_aleatorias) < n:
        u1 = np.random.uniform(0, 1)
        u2 = np.random.uniform(0, 1)
        if u1 <= 1/2:
            variables_aleatorias.append(np.cbrt(u2 - 1))
        else:
            variables_aleatorias.append(np.cbrt(u2))

    return variables_aleatorias
      
        
x = composicion(100000) 

# Graficar el histograma de la muestra generada
plt.figure(figsize=(10, 6))
plt.hist(x, bins=100, density=True, alpha=0.7, edgecolor='black')
plt.xlabel('x')
plt.ylabel('Densidad')
plt.title('Método de composición (a)')
plt.grid(True)

# Graficar la función de masa de probabilidad
x = np.linspace(-1, 1, 100)
y = [funcion_densidad(xi) for xi in x]
plt.plot(x, y, 'r-', linewidth=2, label='Función de densidad teórica')
plt.legend()

plt.tight_layout()
plt.show()