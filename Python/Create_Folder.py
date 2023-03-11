import os
import string

# Запрос номера сложности у пользователя
difficulty = input("Введите Kyu: ")

# Запрос названия папки у пользователя
folder_name_input = input("Введите название: ")

# Замена элементов пунктуации и пробелов на _
folder_name = ''.join(
    c if c not in string.punctuation and not c.isspace() else '_' for c in folder_name_input)

# Создание папки с заданным номером сложности и названием
folder_path = f"Python/{difficulty}_{folder_name}"
os.makedirs(folder_path)

# Создание файлов readme.md и main.py в созданной папке
with open(os.path.join(folder_path, "readme.md"), "w") as f:
    # первая строка начинается с ## и содержит название папки
    f.write("## " + difficulty + " Kyu - " +
            folder_name_input + "\n" + "---\n")

with open(os.path.join(folder_path, "main.py"), "w") as f:
    # первая строка начинается с # и содержит название папки
    f.write("# " + difficulty + " Kyu - " + folder_name_input + "\n")
