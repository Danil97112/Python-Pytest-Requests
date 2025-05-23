import requests

url = "https://api.pokemonbattle.ru/v2/pokemons"  # Замените на фактический URL
Token = "2279cf2951f8a14fd9a0da2aa56dec01" 
headers = {
    "Content-Type": "application/json","trainer_token": Token  # Убедитесь, что заголовок соответствует требованиям API
}

data = {
    "name": "generate",
    "photo_id": -1
}

#response = requests.post(url, headers=headers, json=data)

#print(response.json())  # Выводим ответ от сервера

url1 = "https://api.pokemonbattle.ru/v2/pokemons"  # Замените на фактический URL
Token = "2279cf2951f8a14fd9a0da2aa56dec01" 
headers1 = {
    "Content-Type": "application/json","trainer_token": Token  # Убедитесь, что заголовок соответствует требованиям API
}

data1 = {
    "pokemon_id": "323433",
    "name": "Успешный",
    "photo_id": 2
}

#response = requests.put(url1, headers=headers1, json=data1)

#print(response.json())  # Выводим ответ от сервера

url2 = "https://api.pokemonbattle.ru/v2/trainers/add_pokeball"  # Замените на фактический URL
Token = "2279cf2951f8a14fd9a0da2aa56dec01" 
headers2 = {
    "Content-Type": "application/json","trainer_token": Token  # Убедитесь, что заголовок соответствует требованиям API
}

data2 = {
    "pokemon_id": "323433"
}

response = requests.post(url2, headers=headers2, json=data2)

print(response.json())  # Выводим ответ от сервера