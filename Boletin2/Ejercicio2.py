from multiprocessing import Process, Queue
from random import randint
from time import sleep


def generarDirecionesIP(cola: Queue):
    for _ in range(10):
        direccionip=""
        for _ in range(4):
            num =randint(0, 255)
            direccionip += str(num)+"."
        cola.put(direccionip)  
    cola.put(None)  



def filtarIpPorClases(cola: Queue):
    while True:
        cojerIp = cola.get()  # Espera por datos de la cola
        if cojerIp is None:  # Comprueba si es el marcador de fin
            break
        ip = cojerIp
        sleep(1)  
        clase =obtener_clase_ip(ip)
        imprimirIp(ip,clase)



def obtener_clase_ip(ip):
    primer_octeto = int(ip.split('.')[0])  # Extraer el primer octeto
    if 0 <= primer_octeto <= 127:
        return "Clase A"
    elif 128 <= primer_octeto <= 191:
        return "Clase B"
    elif 192 <= primer_octeto <= 223:
        return "Clase C"
    elif 224 <= primer_octeto <= 239:
        return "Clase D (Multicast)"
    elif 240 <= primer_octeto <= 255:
        return "Clase E (Experimental)"
    else:
        return "IP inválida"


def imprimirIp(ip , clase):
        print(f"La ip es  {ip} y su clase es  '{clase}'")



if __name__ == "__main__":
    # Cola que sirve para manejar datos entre procesos; almacena números
    queue = Queue()

    # Proceso encargado de leer el archivo y añadir datos a la cola
    procesoIntroducirDatosEnCola = Process(target=generarDirecionesIP, args=(queue,))
    # Proceso encargado de procesar los datos de la cola
    procesoManejarDatosEnCola = Process(target=filtarIpPorClases, args=(queue,))
    # Inicia ambos procesos
    procesoIntroducirDatosEnCola.start()
    procesoManejarDatosEnCola.start()

    # Espera a que ambos procesos terminen
    procesoIntroducirDatosEnCola.join()
    procesoManejarDatosEnCola.join()
