import requests

url = "https://api.pokemonbattle.ru/v2/pokemons"  
url2 = "https://api.pokemonbattle.ru/v2/trainers/add_pokeball" 
Token = "token" 
headers = {
    "Content-Type": "application/json","trainer_token": Token  }

data = {
    "name": "generate",
    "photo_id": -1
}

data1 = {
    "pokemon_id": "323433",
    "name": "Успешный",
    "photo_id": 2
}

data2 = {
    "pokemon_id": "323433"
}

response = requests.post(url, headers=headers, json=data)
print(response.json())  

 
response = requests.put(url, headers=headers, json=data1)
print(response.json())  


response = requests.post(url2, headers=headers, json=data2)
print(response.json())  