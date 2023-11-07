# utils.py

import requests
from basic_word import BasicWord # Импорт класса BasicWord из модуля basic_word

def load_random_word():
    json_url = "https://jsonkeeper.com/b/K73Q"  # Замените на ваш URL JSON

    response = requests.get(json_url, verify=False)

    if response.status_code == 200:
        # Проверяем успешный ответ сервера (HTTP 200 OK)
        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            # Проверяем, что полученный JSON - это список и содержит элементы
            # Берем первый элемент из списка (предполагая, что он содержит словарь с данными)
            word_data = data[0]
            # Создаем экземпляр класса BasicWord, используя данные из JSON
            return BasicWord(word_data["word"], word_data["subwords"])
        else:
            # Возвращаем экземпляр класса BasicWord с "default_word" в случае пустых данных
            return BasicWord("default_word", [])
    else:
        # Возвращаем экземпляр класса BasicWord с "default_word" в случае неуспешного запроса
        return BasicWord("default_word", [])
