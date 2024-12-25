import os
from pdf2docx import Converter
from docx2pdf import convert
from PIL import Image

def change_directory():
    new_dir = input("Введите новый рабочий каталог: ")
    if os.path.isdir(new_dir):
        os.chdir(new_dir)
        print(f"Рабочий каталог изменён на: {os.getcwd()}")
    else:
        print("Указанный каталог не существует.")

def pdf_to_docx():
    files = [f for f in os.listdir() if f.endswith('.pdf')]
    if not files:
        print("Нет PDF-файлов для конвертации.")
        return
    for idx, file in enumerate(files, start=1):
        print(f"{idx}. {file}")
    choice = int(input("Введите номер файла для преобразования (или 0 для всех): "))
    if choice == 0:
        for file in files:
            convert_pdf_to_docx(file)
    else:
        convert_pdf_to_docx(files[choice - 1])

def convert_pdf_to_docx(file):
    docx_file = file.replace('.pdf', '.docx')
    cv = Converter(file)
    cv.convert(docx_file)
    cv.close()
    print(f"Файл {file} преобразован в {docx_file}.")

def docx_to_pdf():
    files = [f for f in os.listdir() if f.endswith('.docx')]
    if not files:
        print("Нет DOCX-файлов для конвертации.")
        return
    for idx, file in enumerate(files, start=1):
        print(f"{idx}. {file}")
    choice = int(input("Введите номер файла для преобразования (или 0 для всех): "))
    if choice == 0:
        convert('.')
    else:
        convert(files[choice - 1])
    print("Конвертация завершена.")

def compress_images():
    files = [f for f in os.listdir() if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    if not files:
        print("Нет изображений для сжатия.")
        return
    for idx, file in enumerate(files, start=1):
        print(f"{idx}. {file}")
    choice = int(input("Введите номер файла для сжатия (или 0 для всех): "))
    quality = int(input("Введите уровень качества (1-100): "))
    if choice == 0:
        for file in files:
            compress_image(file, quality)
    else:
        compress_image(files[choice - 1], quality)

def compress_image(file, quality):
    img = Image.open(file)
    img.save(file, optimize=True, quality=quality)
    print(f"Изображение {file} сжато с качеством {quality}.")

def delete_files():
    print("1. Удалить все файлы, начинающиеся на определённую подстроку")
    print("2. Удалить все файлы, заканчивающиеся на определённую подстроку")
    print("3. Удалить все файлы, содержащие определённую подстроку")
    print("4. Удалить все файлы по расширению")
    choice = int(input("Введите номер действия: "))
    substring = input("Введите подстроку или расширение: ")
    files = []
    if choice == 1:
        files = [f for f in os.listdir() if f.startswith(substring)]
    elif choice == 2:
        files = [f for f in os.listdir() if f.endswith(substring)]
    elif choice == 3:
        files = [f for f in os.listdir() if substring in f]
    elif choice == 4:
        files = [f for f in os.listdir() if f.endswith(f".{substring}")]
    for file in files:
        os.remove(file)
        print(f"Файл {file} удалён.")

def main():
    while True:
        print(f"Текущий каталог: {os.getcwd()}")
        print("Выберите действие:")
        print("0. Сменить рабочий каталог")
        print("1. Преобразовать PDF в DOCX")
        print("2. Преобразовать DOCX в PDF")
        print("3. Произвести сжатие изображений")
        print("4. Удалить группу файлов")
        print("5. Выход")
        choice = int(input("Ваш выбор: "))
        if choice == 0:
            change_directory()
        elif choice == 1:
            pdf_to_docx()
        elif choice == 2:
            docx_to_pdf()
        elif choice == 3:
            compress_images()
        elif choice == 4:
            delete_files()
        elif choice == 5:
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
