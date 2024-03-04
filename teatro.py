import numpy as np
np.random.seed(2)

class Theatre_Queue:
    """Definir la clase"""
    def __init__(self, tiempo_total):
        """Inicializacion de la funcion"""
        
        # Parámetros de entrada
        self.media_entre_llegada_fisica = 12.0
        self.media_entre_llegada_telefonica = 10.0
        self.media_servicio_fisico = 6.0
        self.media_servicio_telefonico = 5.0
        self.tiempo_total = tiempo_total #tiempo total de la simulacion

        # Variables de estado
        self.estado_servidor = 0 # 0 es disponible y 1 es ocupado
        self.numero_clientes_cola_fisica = 0
        self.numero_clientes_cola_telefonica = 0
        self.tiempo_llegada_fisica = [] # Lista para el tiempo de llegada fisica
        self.tiempo_llegada_telefonica = [] # Lista para el tiempo de llegada telefonica
        self.tiempo_ultimo_evento = 0.0

        # Contadores estadísticos
        self.num_clientes_fisicos_demorados = 0
        self.num_clientes_telefonicos_demorados = 0
        self.total_demora_fisica = 0.0
        self.total_demora_telefonica = 0.0
        self.area_numero_clientes_cola_fisica = 0.0
        self.area_numero_clientes_cola_telefonica = 0.0
        self.area_estado_servidor = 0.0

        # Reloj de simulación
        self.sim_time = 0.0

        # Lista de eventos
        self.tiempo_siguiente_evento = [0,0,0,0,0] #Esta lista tiene 3 entradas, con el índice 0 no usado
        # 1 llegada fisica, 2 llegada telefonica, 3 salida, 4 parametro de salida de la simulacion
        self.tiempo_siguiente_evento[1] = 2.000
        self.tiempo_siguiente_evento[2] = 3.000
        self.tiempo_siguiente_evento[3] = float('inf')
        self.tiempo_siguiente_evento[4] = self.tiempo_total

        # Otras variables
        self.num_events = 4

    def main(self):

        print("-"*40)
        print("Simulacion de teatro")
        print("Media de llegada entre clientes fisicos: {:.3f} minutos".format(self.media_entre_llegada_fisica))
        print("Media de llegada entre clientes telefonicos: {:.3f} minutos".format(self.media_entre_llegada_telefonica))
        print("Media de servicio en el servicio fisico: {:.3f} minutes".format(self.media_servicio_fisico))
        print("Media de servicio en el servicio telefonico: {:.3f} minutes".format(self.media_servicio_telefonico))
        print("Numero de minutos hasta el fin de la simulacion: {}".format(self.tiempo_total))
        print("-"*40)
        
        while True:
            # Determina cuál es el próximo evento
            self.timing()

            # Actualiza las estadísticas
            self.update_time_avg_stats()

            # Llama la función que le corresponde al evento (tipo 1 es llegada fisica, tipo 2 llegada telefonica, tipo 3 salida y el 4 es el fin de la simulacion)
            if(self.tipo_siguiente_evento == 1):
                self.arrivalPhysical()
            elif(self.tipo_siguiente_evento == 2):
                self.arrivalTelephone()
            elif(self.tipo_siguiente_evento == 3):
                self.departure()
            elif(self.tipo_siguiente_evento == 4):
                break
            
        #se finaliza con un reporte de los resultados de la simulacion
        self.report()

    #funcion de generacion de numeros aleatorios
    def expon(self, mean):
        return (-mean * np.log(np.random.uniform(0,1)))

    #funcion para determinar el siguiente evento de la simulacion
    def timing(self):

        self.minuto_siguiente_evento = float('inf')
        self.tipo_siguiente_evento = 0

        #Inicia comparando inf con el primer elemento de la lista de eventos, posteriormente compara el resto de la lista buscando el valor de tiempo mas pequeño
        for i in range(1, self.num_events+1):
            if(self.tiempo_siguiente_evento[i]<self.minuto_siguiente_evento):
                self.minuto_siguiente_evento = self.tiempo_siguiente_evento[i]
                self.tipo_siguiente_evento = i

        if (self.tipo_siguiente_evento == 0) :
            raise Exception ("Toda entrada en la lista de eventos es infinita, se opta por finalizar la simulacion")

        # El reloj de la simulacion avanza al menor valor numerico posible, es decir, al evento mas cercano
        self.sim_time = self.minuto_siguiente_evento

    def arrivalPhysical(self):
        #Se agenda una nueva llegada fisica
        self.tiempo_siguiente_evento[1] = self.sim_time + self.expon(self.media_entre_llegada_fisica)

        #Si el server está ocupado simplemente se agrega al cliente a la cola, así como su tiempo de llegada
        if(self.estado_servidor == 1):
            self.numero_clientes_cola_fisica+=1
            self.tiempo_llegada_fisica.append(self.sim_time)
        else:
            self.delay = 0.0
            self.total_demora_fisica+=self.delay

            self.num_clientes_fisicos_demorados += 1
            self.estado_servidor = 1

            self.tiempo_siguiente_evento[3] = self.sim_time + self.expon(self.media_servicio_fisico)

    def arrivalTelephone(self):
        #La explicación de este método es recíproca al de arrivalPhysical
        self.tiempo_siguiente_evento[2] = self.sim_time + self.expon(self.media_entre_llegada_telefonica)

        if(self.estado_servidor == 1):
            self.numero_clientes_cola_telefonica+=1
            self.tiempo_llegada_telefonica.append(self.sim_time)
        else:
            self.delay = 0.0
            self.total_demora_telefonica+=self.delay

            self.num_clientes_telefonicos_demorados += 1
            self.estado_servidor = 1

            self.tiempo_siguiente_evento[3] = self.sim_time + self.expon(self.media_servicio_telefonico)
    
    def departure(self):
        # Verifica si la cola fisica está vacía
        if (self.numero_clientes_cola_fisica == 0):

            # Verifica que la cola telefonica este vacia
            if(self.numero_clientes_cola_telefonica == 0):
                self.estado_servidor = 0
                self.tiempo_siguiente_evento[3] = float('inf')

            #En caso de no estarlo, el siguiente cliente telefonico ocupa el servicio
            else:
                self.numero_clientes_cola_telefonica -= 1

                self.delay = self.sim_time - self.tiempo_llegada_telefonica[0]
                self.total_demora_telefonica += self.delay

                self.num_clientes_telefonicos_demorados += 1
                self.tiempo_siguiente_evento[3] = self.sim_time + self.expon(self.media_servicio_telefonico)

                del self.tiempo_llegada_telefonica [0]
        else: # Si la cola fisica no esta vacia

            self.numero_clientes_cola_fisica -= 1

            # Calcula la demora del cliente que empieza el sevicio
            self.delay = self.sim_time - self.tiempo_llegada_fisica[0]
            self.total_demora_fisica += self.delay

            # Incrementa el número de clientes retrasados y agenda una partida
            self.num_clientes_fisicos_demorados += 1
            self.tiempo_siguiente_evento[3] = self.sim_time + self.expon(self.media_servicio_fisico)

            # Elimina el cliente que está de primeras en la fila
            del self.tiempo_llegada_fisica [0]
    
    def report(self):
        
        print("Número de clientes que tuvieron servicio físico {} clientes".format(self.num_clientes_fisicos_demorados))
        print("Número de clientes que tuvieron servicio telefonico {} clientes".format(self.num_clientes_telefonicos_demorados))
        print("Media de demora en la fila física: {:.3f} minutos".format(self.total_demora_fisica/self.num_clientes_fisicos_demorados))
        print("Media de demora en la dila telefónica: {:.3f} minutos".format(self.total_demora_telefonica/self.num_clientes_telefonicos_demorados))
        print("Media de clientes en la fila física: {:.3f} minutos".format(self.area_numero_clientes_cola_fisica/self.sim_time))
        print("Media de clientes en al fila telefónica: {:.3f} minutos".format(self.area_numero_clientes_cola_telefonica/self.sim_time))
        print("Utilización del servicio: {:.3f} minutos".format(self.area_estado_servidor/self.sim_time)) 
        print("Tiempo total de simulación: {:.3f} minutes".format(self.sim_time))
        print("-"*40)
    
    def update_time_avg_stats(self):

        #Calcula el tiempo desde el último evento 
        self.time_since_last_event = self.sim_time - self.tiempo_ultimo_evento
        self.tiempo_ultimo_evento = self.sim_time

        # Actualiza el área bajo la curva de la variable número en cola
        self.area_numero_clientes_cola_fisica += self.numero_clientes_cola_fisica * self.time_since_last_event
        self.area_numero_clientes_cola_telefonica += self.numero_clientes_cola_telefonica * self.time_since_last_event
        self.area_estado_servidor += self.estado_servidor * self.time_since_last_event

m = Theatre_Queue(480)
m.main()