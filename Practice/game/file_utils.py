import os

def load_words(file_path="words.txt"):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            words = file.read().strip().splitlines()
        if not words:
            raise ValueError("Файл слов пуст.")
        return words
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_path} не найден. Проверьте путь и попробуйте снова.")
    except Exception as e:
        raise Exception(f"Ошибка при загрузке слов: {e}")

def load_record(file_path="record.txt"):
    if not os.path.exists(file_path):
        return 0
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return int(file.read().strip() or 0)
    except ValueError:
        return 0 

def save_record(record, file_path="record.txt"):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(str(record))
    except Exception as e:
        raise Exception(f"Ошибка при сохранении рекорда: {e}")

