# players.py

class Player:
    """
    Класс, представляющий игрока с именем и использованными словами.

    Атрибуты:
        username (str): Имя игрока.
        used_words (list): Список слов, использованных игроком.
    """

    def __init__(self, username):
        """
        Инициализация экземпляра класса Player с предоставленным именем игрока.

        Args:
            username (str): Имя игрока.
        """
        self.username = username
        self.used_words = []

    def get_used_word_count(self):
        """
        Получение количества использованных слов игроком.

        Returns:
            int: Количество использованных слов.
        """
        return len(self.used_words)

    def add_used_word(self, word):
        """
        Добавление слова в список использованных слов.

        Args:
            word (str): Слово для добавления.
        """
        self.used_words.append(word)

    def is_word_used(self, word):
        """
        Проверка, было ли слово уже использовано игроком.

        Args:
            word (str): Слово для проверки.

        Returns:
            bool: True, если слово уже было использовано, в противном случае False.
        """
        return word in self.used_words

    def __repr__(self):
        """
        Возврат строкового представления экземпляра класса Player.

        Returns:
            str: Строка, представляющая имя игрока и количество использованных слов.
        """
        return f"Игрок: {self.username}, Использованные слова: {', '.join(self.used_words)}"
