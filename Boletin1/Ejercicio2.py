from multiprocessing import Pool
from time import sleep

def sumaDeNumeros(id, num):
    suma = 0
    for x in range(1,num+1):
        suma +=1
        print ("Proceso " + str(id) + ": Suma de todos los valores hasta el "+ str(x) + ": "+ str(suma))
        sleep(1)
    return suma 


if __name__=="__main__":
        # Declaraciom De pool processes uindica el num de procesos que se ejecutaran al mismo tiempo
    with Pool(processes=2) as pool:

        #tupla     id,num
        numeros = [(1,20),(2,2)]
        # starmap sirve si la rupla tiene varios parametros (1,20) id y numero si no tiene varios parametros usar simplemente map
        resultado = pool.starmap(sumaDeNumeros,numeros) 
    
    print(resultado)





