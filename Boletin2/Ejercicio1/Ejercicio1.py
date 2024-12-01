
from multiprocessing import Process, Queue
from time import sleep

 

def leerFichero(cola: Queue):
    with open("Boletin2\\Ejercicio1\\Ejercicio1.txt", "r") as archivo:
        textoCompleto=""
        for linea in archivo.readlines():    
            textoCompleto += linea 
        textoCompleto= textoCompleto.lower()
        cola.put((textoCompleto,"a"))
        cola.put((textoCompleto,"e"))
        cola.put((textoCompleto,"i"))
        cola.put((textoCompleto,"o"))
        cola.put((textoCompleto,"u"))
        cola.put(None)




def contarLetras(cola: Queue):
    while True:
        cojerLista = cola.get()  # Espera por datos de la cola
        if cojerLista is None:  # Comprueba si es el marcador de fin
            break
        textoCompleto, letra = cojerLista
        contador=0
        sleep(1)  
        for x in  textoCompleto:
            if x == letra:
                contador+=1
        print(f"Hay un total de {contador} letras '{letra}'")

if __name__ == "__main__":
    # Cola que sirve para manejar datos entre procesos; almacena números
    queue = Queue()

    # Proceso encargado de leer el archivo y añadir datos a la cola
    procesoIntroducirDatosEnCola = Process(target=leerFichero, args=(queue,))
    # Proceso encargado de procesar los datos de la cola
    procesoManejarDatosEnCola = Process(target=contarLetras, args=(queue,))

    # Inicia ambos procesos
    procesoIntroducirDatosEnCola.start()
    procesoManejarDatosEnCola.start()

    # Espera a que ambos procesos terminen
    procesoIntroducirDatosEnCola.join()
    procesoManejarDatosEnCola.join()
