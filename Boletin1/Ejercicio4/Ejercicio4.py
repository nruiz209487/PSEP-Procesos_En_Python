from multiprocessing import Pipe, Process
from time import sleep


# Función que lee un archivo de texto línea por línea y coloca los números en la cola.
# Cuando el archivo termina, introduce None en la cola para indicar que no hay más datos.
def leerFichero(pipe):
    with open("Boletin1\Ejercicio4\Ejercicio4.txt", "r") as archivo:
        for linea in archivo.readlines():    
            num = int(linea)  # Convierte cada línea en un número entero
            # Introduce el número en la cola
            pipe.send(num)
            print("Añadiendo: " + str(num))
        # Introduce None en la cola para indicar que no habrá más elementos
        pipe.send(None) 
        pipe.close()


# Función que procesa números de la cola. Se ejecuta repetidamente mientras la cola no contenga None.
def sumaDeNumeros(pipe):
    # Obtiene el primer número de la cola
    num = pipe.recv()
    sleep(1)  # Simula tiempo de procesamiento
    # Se ejecuta mientras no se reciba None en la cola
    while num is not None:
        suma = 0
        # Calcula la suma de los números desde 1 hasta el valor de num
        for x in range(1, num + 1):
            suma += x
        print("Suma hasta " + str(num) + ": " + str(suma))
        # Obtiene el siguiente número de la cola
        num = pipe.recv()
    pipe.close()


if __name__ == "__main__":

    pipe1, pipe2 = Pipe()
    # Proceso encargado de leer el archivo y añadir datos a la cola
    procesoIntroducirDatosEnCola = Process(target=leerFichero, args=(pipe1,))
    # Proceso encargado de procesar los datos de la cola
    procesoManejarDatosEnCola = Process(target=sumaDeNumeros, args=(pipe2,))

    # Inicia ambos procesos
    procesoIntroducirDatosEnCola.start()
    procesoManejarDatosEnCola.start()

    # Espera a que ambos procesos terminen
    procesoIntroducirDatosEnCola.join()
    procesoManejarDatosEnCola.join()
