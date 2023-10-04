# Ejemplo de uso excesivo de ram
import time

lista_contenidos = []

def operacion_intensiva():

    with open('example.txt', 'r') as archivo:
        contenido = archivo.read()
    return contenido

while True:
    time.sleep(.1)
    lista_contenidos.append(operacion_intensiva())