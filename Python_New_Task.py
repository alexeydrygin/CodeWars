import os
import string
import requests
from googletrans import Translator
from bs4 import BeautifulSoup
import re
import sys


os.system('cls' if os.name == 'nt' else 'clear') # очистить содержимое окна консоли

try: # Проверка соединения с интернетом
    requests.get('https://www.codewars.com/')
    text = "Подключение к CodeWars: Готово!"
    sys.stdout.write('\r' + text + '\n')
except requests.exceptions.RequestException as e:
    print('Отсутствует подключение к интернету. Проверьте ваше подключение и повторите попытку.')
    exit()

url = input("\nВведите URL задачи: ") # Введите URL-адрес страницы задачи CodeWars здесь

kata_id = url.split('/')[-1] # Извлекаем ID задачи из URL-адреса

response = requests.get(f'https://www.codewars.com/api/v1/code-challenges/{kata_id}') # Создаем API-запрос, чтобы получить данные о задаче
html = response.content

soup = BeautifulSoup(html, "html.parser") # создаем объект BeautifulSoup

rank_element = response.json().get('rank') # ищем элементы, содержащие информацию о ранге и названии задачи
rank_text = rank_element.get('name') if rank_element else "0 kyu"
title_text = response.json()['name'] if response.json()['name'] else 'unknown title'

prefix = "## " + f"{rank_text}" + " - " + f"{title_text}\n" + "[Ссылка на задачу](" + f"{url}" + ' "' + f"{title_text}" + '")\n\n' # объединяем текст ранга и названия задачи с ссылкой на задачу

kata_description_en = response.json()['description'] # Извлекаем описание задачи из ответа API

if 'http' in kata_description_en: #заменить все вхождения подстроки http на https в переменной kata_description_en
    kata_description_en = kata_description_en.replace('http', 'https')

kata_description_en = prefix + kata_description_en # добавляем префикс в начало kata_description_en

translator = Translator() # Создаем экземпляр класса Translator

kata_description_ru = translator.translate(kata_description_en, dest='ru').text # Переводим описание задачи на русский язык

if '`` `' in kata_description_ru: #заменить все вхождения подстроки `` ` на ``` в переменной kata_description_ru
    kata_description_ru = kata_description_ru.replace('`` `', '```')

kata_description_ru += '\n\n---\n\nВведите описание решения задачи здесь.' # Добавляем дополнительный текст в конец описания задачи на русском языке

difficulty = int(re.findall('\d+', rank_text)[0]) # номер сложности из ранга 

folder_name = ''.join(
    c if c not in string.punctuation and not c.isspace() else '_' for c in title_text) # Замена элементов пунктуации и пробелов на _

folder_path = f"Python/{difficulty}_{folder_name}" # Создание папки с заданным номером сложности и названием
os.makedirs(folder_path)

with open(os.path.join(folder_path, "readme.md"), "w", encoding = "UTF-8") as f: # Создание файлов readme.md и main.py в созданной папке
    f.write(kata_description_en + "\n\n---\n## Задание:\n\n" + kata_description_ru) # первая строка начинается с ## и содержит название папки
with open(os.path.join(folder_path, "main.py"), "w") as f:
    f.write("# " + rank_text +" - " + title_text + "\n") # первая строка начинается с # и содержит название папки

print(f"\nПапка {difficulty}_{folder_name} создана успешно.")