import os
import string
import requests
from googletrans import Translator
from bs4 import BeautifulSoup
import re

# Введите URL-адрес страницы задачи CodeWars здесь
url = input("\nВведите URL задачи: ")

# Извлекаем ID задачи из URL-адреса
kata_id = url.split('/')[-1]

# Создаем API-запрос, чтобы получить данные о задаче
response = requests.get(f'https://www.codewars.com/api/v1/code-challenges/{kata_id}')
html = response.content

# создаем объект BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# ищем элементы, содержащие информацию о ранге и названии задачи
rank_element = response.json()['rank']
if rank_element:
    rank_text = rank_element['name']
else:
    rank_text = 'unknown rank'
title_element = response.json()['name']
if title_element:
    title_text = title_element
else:
    title_text = 'unknown title'

# объединяем текст ранга и названия задачи с ссылкой на задачу
prefix = "## " + f"{rank_text}" + " - " + f"{title_text}\n" + "[Ссылка на задачу](" + f"{url}" + ' "' + f"{title_text}" + '")\n\n'

# Извлекаем описание задачи из ответа API
kata_description_en = response.json()['description']

#заменить все вхождения подстроки http на https в переменной kata_description_en
if 'http' in kata_description_en:
    kata_description_en = kata_description_en.replace('http', 'https')

# добавляем префикс в начало kata_description_en
kata_description_en = prefix + kata_description_en

# Создаем экземпляр класса Translator
translator = Translator()

# Переводим описание задачи на русский язык
kata_description_ru = translator.translate(kata_description_en, dest='ru').text

#заменить все вхождения подстроки `` ` на ``` в переменной kata_description_ru
if '`` `' in kata_description_ru:
    kata_description_ru = kata_description_ru.replace('`` `', '```')

# Добавляем дополнительный текст в конец описания задачи на русском языке
kata_description_ru += '\n\n---\n\nВведите описание решения задачи здесь.'

# номер сложности из ранга 
difficulty  = int(re.findall('\d+', rank_text)[0])

# Замена элементов пунктуации и пробелов на _
folder_name = ''.join(
    c if c not in string.punctuation and not c.isspace() else '_' for c in title_text)

# Создание папки с заданным номером сложности и названием
folder_path = f"Python/{difficulty}_{folder_name}"
os.makedirs(folder_path)

# Создание файлов readme.md и main.py в созданной папке
with open(os.path.join(folder_path, "readme.md"), "w", encoding = "UTF-8") as f:
    # первая строка начинается с ## и содержит название папки
    f.write(kata_description_en + "\n\n---\n## Задание:\n\n" + kata_description_ru)
with open(os.path.join(folder_path, "main.py"), "w") as f:
    # первая строка начинается с # и содержит название папки
    f.write("# " + rank_text +" - " + title_text + "\n")

print(f"\nПапка {difficulty}_{folder_name} создана успешно.")