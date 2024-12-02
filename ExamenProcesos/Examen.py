from multiprocessing import Queue,Process
import random
import os
from time import sleep

#Lee el Archivo bocatas 15 veces y dependiendo de su tiempo de preparacion y un numero aleatorio los anyade a la cola (Mi forma de simular aleatoriedad)
def leerFicheroCrearPedidios(cola: Queue):
    for _ in  range(15):
        numeroAleatorio = random.randint(1, 5)
        with open("ExamenProcesos\Bocatas.txt", "r") as archivo:
            for linea in archivo.readlines():    
                nombre, tiempoPreparacion = linea.strip().split(':')

                if str(numeroAleatorio) == str(tiempoPreparacion):
                    cola.put((nombre,tiempoPreparacion))  # Almacena como tupla
                    print("Añadiendo: " + str(nombre) + " " +  str(tiempoPreparacion) )
            
        # Introduce None en la cola para indicar que no habrá más elementos
    cola.put(None)
    cola.put(None)


# Proceso 2: pocesso encargado de cocinar platillos
def CocinarPedidios(cola: Queue,cola2: Queue ,id):
    while True:
        # Obtiene el pedidio
        pedidos = cola.get()
        if pedidos is None:  # Si recibe None, termina el proceso
            break
        nombre, tiempoPreparacion = pedidos
        sleep(0.1)  
        # cambiar por sleep(tiempoPreparacion)
        print(f"Listo cocina : {nombre} tiempoPreparacion: {tiempoPreparacion} y la id del cocinero es  " + str(id))
        cola2.put((nombre,tiempoPreparacion))
    cola2.put(None)
    cola2.put(None)

# Proceso 3: Encargado de escribir los datos en el fichero
def escribirFichero(cola: Queue ,id):
    while True:
        pedidos = cola.get()  # Obtiene un pedidio
        if pedidos is None:  # Si recibe None, termina el proceso
            break
        nombre, tiempoPreparacion = pedidos

        # Escribe las los repartos en el archivo correspondiente
        with open(f"ExamenProcesos\Repartos.txt", "a") as archivo:
            archivo.write(f"Se ha repartido {nombre} por el repartidor " + str(id) + "\n")  
        print(f"Guardando: {nombre} + repartido por{id} ")
        # sleep(random.randint(1, 7)) 
        sleep(0.1)

if __name__ == "__main__":

    #Elimina el archivo Repartos si existe 
    if os.path.exists("ExamenProcesos\Repartos.txt"):
        os.remove("ExamenProcesos\Repartos.txt")
    #Primera cola para cojer los datos
    queue = Queue()
    #Segunda cola que hace de intermediario entre procesos
    queue2= Queue()

    #Array
    productores = []
    consumidores = []


    #primer proceso
    procesoIntroducirDatosEnCola = Process(target=leerFicheroCrearPedidios, args=(queue,))
    #segundo proceso con dos cocineros
    for i in range(1,3):
       procesoManejarDatosEnCola = Process(target=CocinarPedidios, args=(queue,queue2,i))
       productores.append(procesoManejarDatosEnCola)
    #tercer proceso con 4 repartidores
    for i in range(1,5):
        escribirDatosEnCola = Process(target=escribirFichero, args=(queue2,i))
        consumidores.append(escribirDatosEnCola)


    #Inicio Porcesos
    procesoIntroducirDatosEnCola.start()
    
    for p in productores:
        p.start()

    for c in consumidores:
        c.start()


  # Esperar a que terminen el primer proceso
    procesoIntroducirDatosEnCola.join()

    # Esperar a que terminen todos los productores
    for p in productores:
        p.join()
        print(f'Productor {p} terminado')

    # Esperar a que terminen todos los consumidores
    for c in consumidores:
        c.join()
        print(f'Consumidor {c} terminado')
