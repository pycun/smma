import asyncio
import aiohttp
import json
import random
import time

list_response = []

async def request_to_pokeaki(session):

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

    async with session.get(endpoint) as response:
        json_response = await response.json()

        nombre = json_response.get('forms')[0].get('name')

        list_response.append(nombre)

        return nombre


async def main():

    async with aiohttp.ClientSession() as session:    
        tasks = [request_to_pokeaki(session) for _ in range(100)]
        await asyncio.gather(*tasks)


if __name__ == '__main__':

    # Registra el tiempo de inicio
    inicio = time.time()

    asyncio.run(main())

    # Registra el tiempo de finalización
    fin = time.time()

    # Calcula el tiempo transcurrido
    tiempo_transcurrido = fin - inicio
    print(list_response)
    print(f"El código tardó {tiempo_transcurrido} segundos en ejecutarse.")