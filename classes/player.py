class Player:

    def __int__(self, name):
        self.name = name
        self.sub_words_used = set()

    def __repr__(self):
        return f"Player( {self.name}, {self.sub_words_used})"

    def get_name(self):
        """
        Возвращает имя пользователя
        :return: имя строкой
        """
        return self.name

    def count_sub_words_used(self):
        """
        Возвращает количество использованных слов
        :return: количество слов числом
        """
        return len(self.sub_words_used)

    def add_sub_word(self, sub_word):
        """
        Добавляет слово в список использованных игроков
        :param sub_word: слово для добавления
        """
        self.sub_words_used.add(sub_word)

    def has_sub_word_used(self, sub_word):
        """
        Проверяет, было ли слово использовано
        :param sub_word: слово для проверки
        :return: Результат проверки в bool
        """
        return sub_word in self.sub_words_used
