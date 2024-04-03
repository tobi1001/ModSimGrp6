import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)

# Función de densidad
def funcion_densidad(x):
    return np.where(x < -1, 0, 
                    np.where(x > 1, 0, (3*(x**2)/2)))

def aceptacion_rechazo(n):
    variables_aleatorias = []
    
    while len(variables_aleatorias) < n:
        u1 = np.random.uniform(0, 1)
        u2 = np.random.uniform(0, 1) 
        y = 2*u1 - 1
        
        if u2 <= y**2:   # Se acepta Y si u2 <= Y**2, de lo contrario se vuelve a generar dos numeros aleatorios
            variables_aleatorias.append(y)
    
    return variables_aleatorias

# Generar una muestra de variables aleatorias
x = aceptacion_rechazo(100000)


# Graficar el histograma de la muestra generada
plt.figure(figsize=(10, 6))
plt.hist(x, bins=100, density=True, alpha=0.7, edgecolor='black')
plt.xlabel('x')
plt.ylabel('Densidad')
plt.title('Método de aceptación y rechazo (a)')
plt.grid(True)

# Graficar la función de probabilidad
x = np.linspace(-1, 1, 100)
y = [funcion_densidad(xi) for xi in x]
plt.plot(x, y, 'r-', linewidth=2, label='Función de densidad teórica')
plt.legend()

plt.tight_layout()
plt.show()
