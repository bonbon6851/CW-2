from config import WORDS_TO_PLAY_URL
from classes.player import Player
import utils


def main():

    print("Программа: Ввведите имя игрока")
    user_input = input()
    player = Player(user_input)
    print(f"Приет, {player.get_name()}!")

    # Собираем обьект случайного слова, используя путь из конфигов
    basic_word = utils.load_randow_word(WORDS_TO_PLAY_URL)

    print(f"Составьте {basic_word.count_sub_words()} слов из слова {basic_word.get_word().upper()}")
    print("Слова должны быть не короче 3 букв")
    print("Чтобы закончить игру, угадайте все слова или напишите \"stop\"")
    print("Поехали, ваше первое слово?)")

    # Играем пока пользователь угадал меньше слов, чем было загадано
    while player.count_sub_words_used() < basic_word.count_sub_words():

        user_input = input()
        # выходим если пользователь заказал выход
        if user_input in ["стоп", "stop"]:
            break

        # слово короче 3 букв
        elif len(user_input) < 3:
            print("Слишком короткое слово")


        # слово вообще есть в basicword
        elif not basic_word.has_sub_word(user_input):
            print("Такое слова нельзя составить")


        # слово еще не было угадано
        elif player.has_sub_word_used(user_input):
            print("Такое слово уже есть")


        else:
            print("Верно!")
            player.add_sub_word(user_input)

    # Статистику дергаем из игрока

    print(f"Игра завершена, вы угадали {player.count_sub_words_used()} слов!")


main()