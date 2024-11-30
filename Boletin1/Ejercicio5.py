from multiprocessing import Process
from time import sleep

# La función incrementa una variable suma y la muestra junto con el ID del proceso y el valor actual de la iteración. Se incluye un retraso de 1 segundo con sleep(1).
def sumaDeNumeros(id, num,num2):
    suma = 0
    if (num>num2):
        variableCambio = num2
        num2 = num
        num = variableCambio
    for x in range(num,num2+1):
        suma += x  
        print ("Proceso " + str(id) + ": Suma de todos los valores hasta el "+ str(x) + ": "+ str(suma))
        sleep(1)

if __name__ == '__main__':
#   nombre proceso     referencia a funcion       id,num
    porceso1 = Process(target=sumaDeNumeros, args=(1,3,4))
    porceso2 = Process(target=sumaDeNumeros, args=(2,3,5))
    porceso3 = Process(target=sumaDeNumeros, args=(3,5,3))
# Ejecucuion de proceso se ejecutan todos al mismo tiempo por lo que salnen de manera desordenada 
    porceso1.start()
    porceso2.start()
    porceso3.start()