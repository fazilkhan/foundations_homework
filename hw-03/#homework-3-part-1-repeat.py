#homework-3-repeat

import requests

# What is the URL to the documentation?

print("https://pokeapi.co/docs/v2")

# What pokemon has the ID of 55?

url = "https://pokeapi.co/api/v2/pokemon/55/"
response = requests.get(url)
data = response.json()

print(f"{data['name']} has the ID of 55.")

# How tall is that pokemon?

print(f"{data['name']} is {data['height'] / 10} meters tall.")

# How many versions of Pokemon games have been released?

url = "https://pokeapi.co/api/v2/version/"
response = requests.get(url)
data = response.json()

print(f"There have been {data['count']} versions of the pokemon game.")

# Print out the name of every electric-type pokemon.

url = "https://pokeapi.co/api/v2/type/electric?limit=100&offset=200"
response = requests.get(url)
data = response.json()

print(len(data['pokemon']))

# What are electric-type Pokemon called in the Korean version of the game?
for name in data['names']:
    if name['language']['name'] == 'ko':
        print(name['name'])

# # Who has a higher speed stat, Eevee or Pikachu?

url = "https://pokeapi.co/api/v2/pokemon/pikachu/"
response = requests.get(url)
data = response.json()

for stat in data['stats']:
    if stat['stat']['name'] == 'speed':
        pikachu_speed = stat['base_stat']
        # print(pikachu_speed)

url = "https://pokeapi.co/api/v2/pokemon/eevee/"
response = requests.get(url)
data = response.json()

for stat in data['stats']:
    if stat['stat']['name'] == 'speed':
        eevee_speed = stat['base_stat']
        # print(eevee_speed)

if pikachu_speed > eevee_speed:
    print("Pikachu is faster than Eevee.")
elif pikachu_speed < eevee_speed:
    print("Eevee is faster than Pikachu.")
else:
    print("They are equally fast.")