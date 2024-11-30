from multiprocessing import Pool
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

if __name__=="__main__":
    # Declaraciom De pool processes uindica el num de procesos que se ejecutaran al mismo tiempo
    with Pool(processes=1) as pool:

        #tupla     id,num
        numeros = [(1,20,22),(2,2,22)]
        # starmap sirve si la rupla tiene varios parametros (1,20) id y numero si no tiene varios parametros usar simplemente map
        resultado = pool.starmap(sumaDeNumeros,numeros) 
    
    print(resultado)

