# Ejemplo, se reparten las peticiones
import json
import multiprocessing
import random
import requests
import time

def request_to_pokeaki(x):

    index = random.randint(0, 10)

    pokemons = [
        'bulbasaur',
        'ivysaur',
        'venusaur',
        'charmander',
        'charmeleon',
        'charizard',
        'squirtle',
        'pikachu',
        'wartortle',
        'blastoise',
        'caterpie',
    ]

    endpoint = F'https://pokeapi.co/api/v2/pokemon/{pokemons[index]}'
    response = requests.get(endpoint)

    dict_response = json.loads(response.content)

    nombre = dict_response.get('forms')[0].get('name')

    return nombre



if __name__ == '__main__':

    # Registra el tiempo de inicio
    inicio = time.time()

    # Crea un Pool con 4 procesos
    pool = multiprocessing.Pool()
    # pool = multiprocessing.Pool(processes=4)

    # Asigna tareas al Pool
    resultados = pool.map(request_to_pokeaki, range(100))

    # Cierra el Pool y espera a que todos los procesos terminen
    pool.close()
    pool.join()

    print(resultados)

    # Registra el tiempo de finalización
    fin = time.time()

    # Calcula el tiempo transcurrido
    tiempo_transcurrido = fin - inicio
    print(f"El código tardó {tiempo_transcurrido} segundos en ejecutarse.")
