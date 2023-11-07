# basic_word.py

class BasicWord:
    """
    Класс, представляющий слово и его подслова.

    Атрибуты:
        original_word (str): Исходное слово.
        subwords (list): Список допустимых подслов, образованных из исходного слова.
    """

    def __init__(self, original_word, subwords):
        """
        Инициализация экземпляра класса BasicWord с предоставленным исходным словом и подсловами.

        Args:
            original_word (str): Исходное слово.
            subwords (list): Список допустимых подслов, образованных из исходного слова.
        """
        self.original_word = original_word
        self.subwords = subwords

    def check_word(self, word):
        """
        Проверка, является ли предоставленное слово допустимым подсловом исходного слова.

        Args:
            word (str): Слово для проверки.

        Returns:
            bool: True, если слово является допустимым подсловом, в противном случае False.
        """
        return word in self.subwords

    def count_subwords(self):
        """
        Получение количества допустимых подслов для исходного слова.

        Returns:
            int: Количество допустимых подслов.
        """
        return len(self.subwords)

    def __repr__(self):
        """
        Возврат строкового представления экземпляра класса BasicWord.

        Returns:
            str: Строка, представляющая исходное слово и его подслова.
        """
        return f"Исходное слово: {self.original_word}, Подслова: {', '.join(self.subwords)}"