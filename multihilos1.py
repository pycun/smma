# Ejemplo, se reparten las peticiones
import json
import random
import requests
import threading
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

    for i in range(100):
        hilo = threading.Thread(target=request_to_pokeaki, args=(i,))
        hilo.start()

    # Registra el tiempo de finalización
    fin = time.time()

    # Calcula el tiempo transcurrido
    tiempo_transcurrido = fin - inicio
    print(list_response)
    print(f"El código tardó {tiempo_transcurrido} segundos en ejecutarse.")
