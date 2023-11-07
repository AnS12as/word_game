# main.py

from players import Player  # Импортируем класс Player из модуля players
from utils import load_random_word  # Импортируем функцию load_random_word из модуля utils

def main():
    # Получаем имя игрока
    player_name = input("Введите ваше имя: ")

    # Создаем экземпляр класса Player с именем игрока
    player = Player(player_name)

    # Приветствуем игрока
    print(f"Привет, {player.username}!")

    # Загружаем случайное слово с помощью функции load_random_word
    word_instance = load_random_word()

    # Отображаем начальное слово
    print(f"Составьте 8 слов из слова {word_instance.original_word}")
    print("Слова должны быть длиной не менее 3 букв.")
    print('Для завершения игры угадайте все слова или введите "stop".')

    # Инициализируем переменные для отслеживания состояния игры
    правильные_угадывания = 0
    всего_слов = 8

    while правильные_угадывания < всего_слов:
        # Просим игрока сделать ход
        слово_ввод = input("Ваше слово: ")

        if слово_ввод == "stop":
            break

        if len(слово_ввод) < 3:
            print("Слово слишком короткое.")
            continue

        if слово_ввод in word_instance.subwords:
            if player.is_word_used(слово_ввод):
                print("Слово уже использовано.")
            else:
                player.add_used_word(слово_ввод)
                правильные_угадывания += 1
                print("Верно!")
        else:
            print("Неверное слово.")

    # Отображаем итоговый счет
    print(f"Игра окончена! Вы угадали {правильные_угадывания} из {всего_слов} слов.")

if __name__ == "__main__":
    main()
