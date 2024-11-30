
from multiprocessing import Process, Queue
from time import sleep


# Función que lee un archivo de texto línea por línea y coloca los números en la cola.
# Cuando el archivo termina, introduce None en la cola para indicar que no hay más datos.
def leerFichero(cola: Queue):
    with open("Boletin1\Ejercicio3\Ejercicio3.txt", "r") as archivo:
        for linea in archivo.readlines():    
            num = int(linea)  # Convierte cada línea en un número entero
            # Introduce el número en la cola
            cola.put(num)
            print("Añadiendo: " + str(num))
        # Introduce None en la cola para indicar que no habrá más elementos
        cola.put(None)


# Función que procesa números de la cola. Se ejecuta repetidamente mientras la cola no contenga None.
def sumaDeNumeros(cola: Queue):
    # Obtiene el primer número de la cola
    num = cola.get()
    sleep(1)  # Simula tiempo de procesamiento
    # Se ejecuta mientras no se reciba None en la cola
    while num is not None:
        suma = 0
        # Calcula la suma de los números desde 1 hasta el valor de num
        for x in range(1, num + 1):
            suma += x
        print("Suma hasta " + str(num) + ": " + str(suma))
        # Obtiene el siguiente número de la cola
        num = cola.get()


if __name__ == "__main__":
    # Cola que sirve para manejar datos entre procesos; almacena números
    queue = Queue()

    # Proceso encargado de leer el archivo y añadir datos a la cola
    procesoIntroducirDatosEnCola = Process(target=leerFichero, args=(queue,))
    # Proceso encargado de procesar los datos de la cola
    procesoManejarDatosEnCola = Process(target=sumaDeNumeros, args=(queue,))

    # Inicia ambos procesos
    procesoIntroducirDatosEnCola.start()
    procesoManejarDatosEnCola.start()

    # Espera a que ambos procesos terminen
    procesoIntroducirDatosEnCola.join()
    procesoManejarDatosEnCola.join()
