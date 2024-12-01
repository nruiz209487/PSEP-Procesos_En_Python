from multiprocessing import Pipe, Process
import random
from time import sleep


def InicializarJugador(pipe):
        pipe.send(("jugador 1 ", 20)) 
        pipe.send(("jugador 2 ", 5)) 
        pipe.send(("jugador 3 ", 12)) 
        pipe.send(("jugador 4 ", 9)) 
        pipe.send(None) 
        pipe.close()

# Función que procesa números de la cola. Se ejecuta repetidamente mientras la cola no contenga None.
def RealizarSorteo(pipe):
    print("Reaizado apuestas:")
    numeros_aleatorios =generar_tupla_unica(1,21,5)
    while True:
        # Obtiene la cola
        obtenerDatos = pipe.recv()
        if obtenerDatos is None  :  # Si recibe None, termina el proceso
            break
        nombre, apuesta = obtenerDatos
        sleep(1)  # Simula tiempo de procesamiento
       
        if apuesta in numeros_aleatorios  :  # Si recibe None, termina el proceso
            print("El jugador " + nombre + "ha acetado")
    pipe.close()

def generar_tupla_unica(rango_inferior, rango_superior, cantidad):
    # Genera la tupla de números aleatorios sin repetirse
    numeros_aleatorios = tuple(random.sample(range(rango_inferior, rango_superior + 1), cantidad))
    print(numeros_aleatorios)
    return numeros_aleatorios


if __name__ == "__main__":

    pipe1, pipe2 = Pipe()
    # Proceso encargado de leer el archivo y añadir datos a la cola
    procesoIntroducirDatosEnCola = Process(target=InicializarJugador, args=(pipe1,))
    # Proceso encargado de procesar los datos de la cola
    procesoManejarDatosEnCola = Process(target=RealizarSorteo, args=(pipe2,))

    # Inicia ambos procesos
    procesoIntroducirDatosEnCola.start()
    procesoManejarDatosEnCola.start()

    # Espera a que ambos procesos terminen
    procesoIntroducirDatosEnCola.join()
    procesoManejarDatosEnCola.join()