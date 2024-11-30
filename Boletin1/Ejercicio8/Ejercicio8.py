from multiprocessing import Pipe, Process
from time import sleep


# Función que lee un archivo de texto línea por línea y coloca los números en la cola.
# Cuando el archivo termina, introduce None en la cola para indicar que no hay más datos.
def leerFichero(pipe):
    with open("Boletin1\Ejercicio8\Ejercicio8.txt", "r") as archivo:
        for linea in archivo.readlines():    
            numeroDeInicio, numeroFinal = map(int, linea.strip().split(','))  # Convierte a enteros
            # Introduce el número en la cola
            pipe.send((numeroDeInicio, numeroFinal))  # Envia una tupla con dos valores
            print("Añadiendo: "+ str(numeroDeInicio) + " " +  str(numeroFinal))
        # Introduce None en la cola para indicar que no habrá más elementos
        pipe.send(None) 
        pipe.close()



# Función que procesa números de la cola. Se ejecuta repetidamente mientras la cola no contenga None.
def sumaDeNumeros(pipe):
    while True:
        # Obtiene el primer número de la cola
        numeros = pipe.recv()
        if numeros is None:  # Si recibe None, termina el proceso
            break
        numeroDeInicio, numeroFinal = numeros
        suma = 0  # Reiniciar suma en cada ciclo
        sleep(1)  # Simula tiempo de procesamiento
        # Asegura que el rango se recorra de menor a mayor
        if numeroDeInicio > numeroFinal:
            numeroDeInicio, numeroFinal = numeroFinal, numeroDeInicio

        # Calcula la suma de los números desde numeroDeInicio hasta numeroFinal
        for x in range(numeroDeInicio, numeroFinal + 1):
            suma += x
        print(f"Suma desde {numeroDeInicio} hasta {numeroFinal}: {suma}")
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




