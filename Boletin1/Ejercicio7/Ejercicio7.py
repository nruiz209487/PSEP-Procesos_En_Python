from multiprocessing import Process, Queue
from time import sleep


# Función que lee un archivo de texto línea por línea y coloca los números en la cola.
# Cuando el archivo termina, introduce None en la cola para indicar que no hay más datos.
def leerFichero(cola: Queue):
    with open("Boletin1\Ejercicio7\Ejercicio7.txt", "r") as archivo:
        for linea in archivo.readlines():    
            numeroDeInicio, numeroFinal = map(int, linea.strip().split(','))  # Convierte a enteros
            # Introduce los números en la cola
            cola.put((numeroDeInicio, numeroFinal))  # Almacena como tupla
            print("Añadiendo: " + str(numeroDeInicio) + " " +  str(numeroFinal) )
        # Introduce None en la cola para indicar que no habrá más elementos
        cola.put(None)



# Función que procesa números de la cola. Se ejecuta repetidamente mientras la cola no contenga None.
def sumaDeNumeros(cola: Queue):
    while True:
        # Obtiene el primer número de la cola
        pedidos = cola.get()
        if pedidos is None:  # Si recibe None, termina el proceso
            break
        numeroDeInicio, numeroFinal = pedidos
        suma = 0  # Reiniciar suma en cada ciclo
        sleep(1)  # Simula tiempo de procesamiento
        # Asegura que el rango se recorra de menor a mayor
        if numeroDeInicio > numeroFinal:
            numeroDeInicio, numeroFinal = numeroFinal, numeroDeInicio

        # Calcula la suma de los números desde numeroDeInicio hasta numeroFinal
        for x in range(numeroDeInicio, numeroFinal + 1):
            suma += x
        print(f"Suma desde {numeroDeInicio} hasta {numeroFinal}: {suma}")


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
