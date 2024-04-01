import simpy
import numpy as np
import matplotlib.pyplot as plt

SEED = 8888
np.random.seed(SEED)
print(f"Usando semilla: {SEED}")

class Taqueria:
    def __init__(self, tiempo_simulacion):

        # Parametros de entrada
        self.tiempo_simulacion = tiempo_simulacion # Tiempo que dura la simulación en minutos
        self.num_mesas_2 = 4 # Numero de mesas con capacidad para 2 personas
        self.num_mesas_4 = 2 # Numero de mesas con capacidad para 4 personas
        self.precio_orden = 400 # Precio por orden
        self.costo_orden = 200 # Costo por orden
        self.salario_mesero = 3000 / 60 # Salario del mesero por minuto

        # Contadores estadísticos
        self.utilidad_total = 0
        self.clientes_sin_mesa = 0
        self.clientes_totales = 0
        self.grupos_totales = 0
        self.max_grupos_cola = 0
        self.tiempo_total_espera = 0
        self.tiempo_total_comida = 0
        self.tamano_total_grupo = 0
        self.tiempo_total_llegadas = 0
        self.grupos_mesa_inmediata = 0

    def main(self):

        # Ejecutar la simulación
        self.env = simpy.Environment()
        self.mesas_2 = simpy.Resource(self.env, capacity=self.num_mesas_2)
        self.mesas_4 = simpy.Resource(self.env, capacity=self.num_mesas_4)
        self.env.process(self.generar_clientes())
        self.env.run(until=self.tiempo_simulacion)

        # Crear lista para almacenar la utilidad acumulada en cada minuto
        self.utilidad_acumulada = []

        # Ejecutar la simulación
        self.env = simpy.Environment()
        self.mesas_2 = simpy.Resource(self.env, capacity=self.num_mesas_2)
        self.mesas_4 = simpy.Resource(self.env, capacity=self.num_mesas_4)
        self.env.process(self.generar_clientes())
        
        # Registrar la utilidad acumulada en cada minuto
        for i in range(1, self.tiempo_simulacion + 1):
            self.env.run(until=i)
            utilidad_actual = self.utilidad_total - (self.salario_mesero * i)
            self.utilidad_acumulada.append(utilidad_actual)

    def cliente(self):  # Proceso que simula un cliente

        ###########
        # LLegada #
        ###########
        tamano_grupo = self.generar_tamano_grupo()  # Genera el tamaño del grupo

        tiempo_comida_grupo = 0.0 # Tiempo que más tarda la persona en comer (máx tiempos)

        utilidad_grupo = 0.0
        for _ in range(tamano_grupo):
            num_ordenes = self.generar_numero_ordenes_por_persona() # Numero de ordenes que pedira esta persona
            tiempo = 0.0 # el tiempo total que se demorara comiendo
            for orden in range(num_ordenes):
                tiempo += self.generar_tiempo_comida_por_orden() # un tiempo distito por cada orden, los acumulamos
                utilidad_grupo += (self.precio_orden - self.costo_orden)

            tiempo_comida_grupo = max(tiempo_comida_grupo,tiempo) # comparamos contra el maximo, dejamos el mayor

        mesas = self.mesas_2 if tamano_grupo <= 2 else self.mesas_4 # Elegimos el conjunto de mesas apropiado
        
        mesa_req = mesas.request()

        llegada = self.env.now # Establece el tiempo de llegada del cliente

        ##########
        # Espera #
        ##########

        yield mesa_req  # Esperamos hasta que haya una mesa libre (que se cumpla la reques por la mesa)

        tiempo_espera = self.env.now - llegada
        if tiempo_espera == 0:
          self.grupos_mesa_inmediata += 1

        self.clientes_sin_mesa += tamano_grupo * tiempo_espera

        #########
        # Tacos #
        #########

        yield self.env.timeout(tiempo_comida_grupo) # Comemos

        mesas.release(mesa_req) # Liberamos la mesa

        # TODO: contar grupos/clientes sin mesa

        # Actualiza las estadísticas
        self.clientes_totales += tamano_grupo
        self.grupos_totales += 1
        self.max_grupos_cola = max(self.max_grupos_cola, len(self.mesas_2.queue) + len(self.mesas_4.queue))
        self.tiempo_total_espera += tiempo_espera
        self.tiempo_total_comida += tiempo_comida_grupo
        self.tamano_total_grupo += tamano_grupo
        self.utilidad_total += utilidad_grupo

    def generar_clientes(self):
        while True:
            tiempo_llegada = self.generar_tiempo_entre_llegada()
            self.tiempo_total_llegadas += tiempo_llegada
            yield self.env.timeout(tiempo_llegada)
            self.env.process(self.cliente()) # Se crea un proceso por cada cliente


    def estadisticas(self):
        utilidad_total = self.utilidad_total - (self.salario_mesero * self.env.now)
        tiempo_promedio_espera = self.tiempo_total_espera / self.grupos_totales
        tiempo_promedio_comida = self.tiempo_total_comida / self.grupos_totales
        tamano_promedio_grupo = self.tamano_total_grupo / self.grupos_totales
        tiempo_promedio_llegadas = self.tiempo_total_llegadas / self.grupos_totales
        probabilidad_sin_mesa = (self.grupos_totales - self.grupos_mesa_inmediata)/self.grupos_totales

        print(f"Utilidad total: ${utilidad_total}")
        print(f"Probabilidad de no encontrar mesa disponible: {probabilidad_sin_mesa:.2%}")
        print(f"Número máximo de grupos en la cola: {self.max_grupos_cola}")
        print(f"Tiempo promedio de espera en la cola: {tiempo_promedio_espera:.2f} minutos")
        print(f"Tiempo promedio de comida por grupo: {tiempo_promedio_comida:.2f} minutos")
        print(f"Tamaño de grupo promedio: {tamano_promedio_grupo:.2f} personas")
        print(f"Tiempo entre llegadas promedio: {tiempo_promedio_llegadas:.2f} minutos")

        # Intervalo de confianza del 95% para la probabilidad de no encontrar mesa
        n = self.grupos_totales
        p = (self.grupos_totales - self.grupos_mesa_inmediata)
        z = 1.96  # Valor crítico para un nivel de confianza del 95%
        proporcion = p/n

        if p == 0 or p == 1:
            intervalo_confianza = (p, p)
        else:
            error_estandar = np.sqrt(proporcion * (1 - proporcion) / n)
            intervalo_confianza = (proporcion - z * error_estandar, proporcion + z * error_estandar)

        print(f"Intervalo de confianza del 95% para la probabilidad de no encontrar mesa: {intervalo_confianza}")

        # Probabilidad de no encontrar mesa con el intervalo de confianza
        plt.figure(figsize=(6, 6))
        plt.bar(['Probabilidad (grupos)'], [(p/n)], color='b', alpha=0.7)
        
        # Longitud del intervalo de confianza
        plt.errorbar(['Probabilidad (grupos)'], [p/n], yerr=[[(p/n) - intervalo_confianza[0]], [intervalo_confianza[1] - (p/n)]],
                    fmt='none', ecolor='r', capsize=5, elinewidth=2, capthick=2)
        
        plt.text(0, (p/n) + 0.1, f"IC 95%: [{intervalo_confianza[0]:.4f}, {intervalo_confianza[1]:.4f}]",
                ha='center', va='bottom', color='black', fontsize=12)
        
        plt.ylabel('Probabilidad')
        plt.title('Probabilidad de no encontrar mesa (95% de confiabilidad)')
        plt.ylim(0, 1)  # Límites del eje y entre 0 y 1
        plt.show()

        # Utilidad acumulada
        plt.figure(figsize=(8, 6))
        plt.plot(range(TIEMPO_SIMULACION), self.utilidad_acumulada)
        plt.xlabel('Tiempo (minutos)')
        plt.ylabel('Utilidad acumulada')
        plt.title('Utilidad acumulada a lo largo del tiempo')
        plt.grid(True)
        plt.show()

    def generar_tiempo_entre_llegada(self): # Tiempo entre llegadas de los clientes (Con el método de transformada inversa)
        u = np.random.uniform(0, 1)
        return (-6 * np.log(1 - u))

    def generar_tamano_grupo(self): # Tamaño del grupo que llega
        return np.random.choice([1, 2, 3], p = [0.4, 0.3, 0.3])

    def generar_numero_ordenes_por_persona(self): # Ordenes de tacos por cliente
        return np.random.choice([0, 1, 2], p = [0.2, 0.65, 0.15])

    def generar_tiempo_comida_por_orden(self): # Tiempo para comer una orden (min/orden)
        return np.random.choice([10, 15, 20, 25], p = [0.1, 0.4, 0.3, 0.2])


TIEMPO_SIMULACION = 60 * 24 # 60 min/hor * 24 horas ~ 1 dia en minutos
model = Taqueria(TIEMPO_SIMULACION)
model.main()
model.estadisticas()