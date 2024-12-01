from multiprocessing import Pool
import random
import os
from time import sleep

# Proceso 1: Generar notas aleatorias con más detalle
def generar_notas(archivo):
    notas = []
    
    # Genera 6 números aleatorios con decimales entre 1 y 10
    for _ in range(6):
        nota = round(random.uniform(1, 10), 2)  # Número aleatorio con dos decimales
        notas.append(nota)
  
    # Escribe las notas en el archivo usando un bucle for
    with open(archivo, "w") as f:
        for nota in notas:
            f.write(str(nota) + "\n")  # Escribe cada nota en una nueva línea
            sleep(0.2)
    print("Notas generadas y guardadas en " + archivo)
    return archivo  # Devuelve el nombre del archivo

# Proceso 2: Calcular la media de las notas
def calcular_media(datos):

    archivo, nombre = datos
    
    # Leer las notas del archivo
    with open(archivo, "r") as f:
        notas = list(map(float, f.readlines()))
    
    # Calcular la media
    media = round(sum(notas) / len(notas), 2)
    
    # Guardar la media en medias.txt
    with open("Boletin2/Ejercicio3/medias.txt", "a") as f_medias:
        f_medias.write(f"{media} {nombre}\n")
    
    return media, nombre

# Proceso 3: Obtener la nota máxima de todas las medias
def obtener_nota_maxima():
    sleep(1)
    print("Obteniendo la nota máxima de medias.txt...")
    
    # Leer las medias de medias.txt
    with open("Boletin2/Ejercicio3/medias.txt", "r") as f:
        lines = f.readlines()
        medias = [(float(line.split()[0]), line.split()[1]) for line in lines]
        max_media = max(medias, key=lambda x: x[0])
        print(f"Nota máxima: {max_media[0]} obtenida por {max_media[1]}")



if __name__ == "__main__":
    # Eliminar el archivo medias.txt si ya existe
    if os.path.exists("Boletin2/Ejercicio3/medias.txt"):
        os.remove("Boletin2/Ejercicio3/medias.txt")

    # Número de alumnos
    num_alumnos = 10

    # Generar los nombres de los alumnos de forma explícita
    nombres = []
    for i in range(num_alumnos):
        nombre = "Alumno" + str(i + 1)
        nombres.append(nombre)

    # Generar las rutas de los archivos para las notas de cada alumno de forma explícita
    txtAlumnos = []
    for i in range(num_alumnos):
        archivo = "Boletin2/Ejercicio3/notas_alumno" + str(i + 1) + ".txt"
        txtAlumnos.append(archivo)

    # Proceso 1: Generar los archivos de notas en paralelo
    with Pool() as pool:
        rutas = pool.map(generar_notas, txtAlumnos)

    # Proceso 2: Calcular la media de cada alumno y almacenarla en medias.txt
    with Pool() as pool:
        pool.map(calcular_media, zip(rutas, nombres))

    # Proceso 3: Obtener y mostrar la nota máxima
    obtener_nota_maxima()
