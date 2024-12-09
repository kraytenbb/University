import random
from game.file_utils import load_words, load_record, save_record

def display_word(word, guessed_letters):
    return "".join(letter if letter in guessed_letters else "■" for letter in word)

def play_round(word, lives):
    guessed_letters = set()
    while lives > 0:
        print(f"\nСлово: {display_word(word, guessed_letters)}")
        print(f"Количество жизней: {'♥' * lives}")
        guess = input("Назовите букву или слово целиком: ").strip().lower()
        if not guess.isalpha():
            print("Ошибка ввода. Введите букву или слово.")
            continue
        
        if len(guess) == 1:
            if guess in guessed_letters:
                print("Вы уже называли эту букву.")
            elif guess in word:
                guessed_letters.add(guess)
                print("Верно!")
            else:
                lives -= 1
                print("Неправильно. Вы теряете жизнь.")
        elif guess == word:
            print(f"Слово отгадано: {word}")
            return True
        else:
            lives -= 1
            print("Неправильно. Вы теряете жизнь.")
        
        if set(word).issubset(guessed_letters):
            print(f"Слово отгадано: {word}")
            return True

    print(f"Вы проиграли. Слово было: {word}")
    return False

def main():
    try:
        words = load_words()
        record = load_record()
        current_score = 0

        print("Добро пожаловать в игру 'Поле чудес'!")
        while words:
            print(f"\nВаш текущий рекорд: {record}. Угаданных слов: {current_score}.")
            difficulty = input("Выберите уровень сложности (лёгкий, средний, сложный): ").strip().lower()
            lives = {"лёгкий": 7, "средний": 5, "сложный": 3}.get(difficulty, 5)

            word = random.choice(words)
            words.remove(word)

            if play_round(word, lives):
                current_score += 1
                print("Поздравляем! Вы выиграли!")
            else:
                break

            if not input("Хотите сыграть ещё раз? (да/нет): ").strip().lower().startswith("д"):
                break

        print(f"Игра завершена. Вы угадали {current_score} слов(а).")
        if current_score > record:
            print(f"Новый рекорд: {current_score}!")
            save_record(current_score)
        else:
            print(f"Ваш рекорд: {record}.")
    except Exception as e:
        print(f"Произошла ошибка: {e}. Попробуйте снова.")
