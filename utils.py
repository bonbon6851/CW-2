import random

import requests as requests

from classes.basic_word import BasicWord


def load_data(path):
    """
    Загружает данные по URL
    :param path: путь к данным
    :return: данные в виде списка или словаря, пустого если ошибка
    """

    result = requests.get(path)

    result_status = result.status_code
    if result_status != 200:
        return []

    return result.json()


def load_randow_word(path):
    """
    Возвращает случайно слово загруженное по переданному адресу
    :param path: путь к данным
    :return: экземпляр BasicWord или None если слово не получилось
    """

    list_of_words = load_data(path)

    if len(list_of_words) == 0:
        return None

    random_word = random.choice(list_of_words)

    word = random_word["word"]
    sub_words = random_word["subwords"]

    basic_word = BasicWord(word, sub_words)

    return basic_word

