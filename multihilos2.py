# Ejemplo, se reparten las peticiones
from concurrent.futures import ThreadPoolExecutor
import json
import random
import requests
import time

list_response = []

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

    list_response.append(nombre)

    return nombre



if __name__ == '__main__':

    # Registra el tiempo de inicio
    inicio = time.time()

    executor =  ThreadPoolExecutor(max_workers=100)
    executor.map(request_to_pokeaki, range(100))
    executor.shutdown(wait=True)

    # Registra el tiempo de finalización
    fin = time.time()

    # Calcula el tiempo transcurrido
    tiempo_transcurrido = fin - inicio
    print(list_response)
    print(f"El código tardó {tiempo_transcurrido} segundos en ejecutarse.")
