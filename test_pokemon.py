import requests

def test_get_trainers_status_code():
    url = "https://api.pokemonbattle.ru/v2/trainers"
    response = requests.get(url)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

import requests

def test_trainer_name_in_response():
    trainer_id = 33249  # Замените на реальный ID вашего тренера
    expected_trainer_name = "Стифлер"  # Замените на имя вашего тренера

    response = requests.get("https://api.pokemonbattle.ru/v2/trainers", params={"trainer_id": trainer_id})
    
    assert response.status_code == 200, "Запрос завершился с ошибкой"
    assert expected_trainer_name in response.text, f"Имя тренера '{expected_trainer_name}' не найдено в ответе"
