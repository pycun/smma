# Ejemplo, se ejecuta peticion por peticion
import json
import random
import requests
import time

def request_to_pokeaki():


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

    forma = dict_response.get('forms')[0].get('name')

    return forma


if __name__ == '__main__':

    list_response = []

    # Registra el tiempo de inicio
    inicio = time.time()

    for i in range(100):

        response = request_to_pokeaki()
        list_response.append(response)


    # Registra el tiempo de finalización
    fin = time.time()

    # Calcula el tiempo transcurrido
    tiempo_transcurrido = fin - inicio
    print(list_response)
    print(f"El código tardó {tiempo_transcurrido} segundos en ejecutarse.")
