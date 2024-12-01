from multiprocessing import Process, Queue
from random import randint
from time import sleep

def producer(q, id):  # función de productor
    for i in range(10):  # envía 10 mensajes
        if q.full():
            print(f'Productor {id}: cola llena')
        elif q.empty():
            print(f'Productor {id}: cola vacía')
        
        q.put(i)  # envía el mensaje número i
        print(f'Productor {id}: {i} enviado')
        sleep(randint(1, 5))  # espera entre 1 y 5 segundos

    q.put(None)  # envía el mensaje None para indicar fin
    print(f'Productor {id}: terminado')

def consumer(q, id):  # función de consumidor
    while True:
        if q.full():
            print(f'Consumidor {id}: cola llena')
        elif q.empty():
            print(f'Consumidor {id}: cola vacía')
        
        item = q.get()  # recibe el mensaje
        if item is None:  # No hay más elementos
            break
        print(f'Consumidor {id}: {item} recibido')
        sleep(randint(1, 5))  # espera 4 segundos tras procesar cada elemento

    print(f'Consumidor {id}: terminado')

if __name__ == '__main__':
    queue = Queue(maxsize=10)  # crea una cola con un tamaño máximo de 10 objetos

    # Crear arrays de productores y consumidores
    productores = []
    consumidores = []

    # Crear 3 productores
    for i in range(3):
        p = Process(target=producer, args=(queue, i))
        productores.append(p)

    # Crear 3 consumidores
    for i in range(3):
        c = Process(target=consumer, args=(queue, i))
        consumidores.append(c)

    # Iniciar procesos de productores
    for p in productores:
        p.start()

    # Iniciar procesos de consumidores
    for c in consumidores:
        c.start()

    # Esperar a que terminen todos los productores
    for p in productores:
        p.join()
        print(f'Productor {p.pid} terminado')

    # Esperar a que terminen todos los consumidores
    for c in consumidores:
        c.join()
        print(f'Consumidor {c.pid} terminado')