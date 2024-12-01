from multiprocessing import Process, Queue
from time import sleep


# Función que lee un archivo de texto línea por línea y coloca los números en la cola.
# Cuando el archivo termina, introduce None en la cola para indicar que no hay más datos.
def leerFichero(cola: Queue , anyoFlitro):
    with open("Boletin2\Ejercicio4\Peliculas.txt", "r") as archivo:
        for linea in archivo.readlines():    
            pelicula, anyo = linea.strip().split(';')
            if(anyoFlitro==anyo):
                cola.put((pelicula,anyo))  # Almacena como tupla
            print("Añadiendo: " + str(pelicula) + " " +  str(anyo) )
        # Introduce None en la cola para indicar que no habrá más elementos
        cola.put(None)



def escribirFichero(cola: Queue):
    while True:
        datosPelicula = cola.get()  # Obtiene una tupla (película, año)
        if datosPelicula is None:  # Si recibe None, termina el proceso
            break
        pelicula, anyo = datosPelicula

        # Escribe las películas en el archivo correspondiente al año
        with open(f"Boletin2\\Ejercicio4\\Peliculas{anyo}.txt", "a") as archivo:
            archivo.write(f"{pelicula};{anyo}\n")  # Escribe la película y el año en el archivo
        print(f"Guardando: {pelicula} {anyo}")
        sleep(1)  # Simula un tiempo de procesamiento


if __name__ == "__main__":
    # Cola que sirve para manejar datos entre procesos; almacena números
    queue = Queue()
    anyo="2000"
    # Proceso encargado de leer el archivo y añadir datos a la cola
    procesoIntroducirDatosEnCola = Process(target=leerFichero, args=(queue,anyo))
    # Proceso encargado de procesar los datos de la cola
    procesoManejarDatosEnCola = Process(target=escribirFichero, args=(queue,))

    # Inicia ambos procesos
    procesoIntroducirDatosEnCola.start()
    procesoManejarDatosEnCola.start()

    # Espera a que ambos procesos terminen
    procesoIntroducirDatosEnCola.join()
    procesoManejarDatosEnCola.join()
