class BasicWord:
    """
    Класс для хранения базового слова и его подслов
    """

    def __int__(self, word, sub_word):
        self.word = word
        self.sub_word = sub_word

    def __repr__(self):
        return f"BasicWord({self.word}, {self.sub_word})"

    def get_word(self):
        """
        Возвращает исходное слово
        :return: слово в виде строки
        """
        return self.word

    def count_sub_words(self):
        """
        Возвращает общее количество подслов
        :return: количество подслов числом
        """
        return len(self.sub_word)

    def has_sub_word(self, word_to_check):
        return word_to_check.strip().lower() in self.sub_word


python_sub_words = ["пони","тон","ион","опт","пот","тип","топ","пион","понт"]
test_word = BasicWord(python_sub_words)

print(test_word)