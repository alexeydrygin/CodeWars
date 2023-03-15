## 6 kyu - Replace With Alphabet Position
[Ссылка на задачу](https://www.codewars.com/kata/546f922b54af40e1e90001da "Replace With Alphabet Position")

Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

`"a" = 1`, `"b" = 2`, etc.

## Example <!-- unlisted languages will use the first entry. please keep python up top. -->

```python
alphabet_position("The sunset sets at twelve o' clock.")
```


Should return `"20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"` ( as a string )


---
## Задание:

## 6 kyu - заменить на позицию алфавита
[SSSLKA na зadaчue] (https://www.codewars.com/kata/546f922b54af40e1e90001da "Заменить на позицию алфавита")

Добро пожаловать.

В этой Kata вы должны, учитывая строку, замените каждую букву на его положение в алфавите.

Если что -то в тексте не является буквой, не обращайте внимания и не возвращайте его.

`" a "= 1`,` "b" = 2` и т. Д.


```Python
alphabet_position («Закат устанавливается в двенадцать часов.»)
```

Должен вернуться `" 20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 5 22 5 15 3 15 15 3 11 "` (в качестве строки)

---

Вот как работает функция:

Создаем строку alphabet, которая содержит все буквы алфавита в нижнем регистре.

Приводим строку text к нижнему регистру, чтобы можно было сравнить каждый символ с буквами алфавита.

Для каждого символа в строке text в нижнем регистре проверяем, находится ли он в alphabet. Если да, вычитаем 96 из его кода ASCII (ord(char)) для получения его позиции в алфавите. Затем добавляем это значение в виде строки в список result.

В конце мы соединяем элементы списка result в одну строку с пробелами в качестве разделителей и возвращаем эту строку.

Чтобы вызвать эту функцию с примером ввода, нужно выполнить следующий код:

```python
text = "The sunset sets at twelve o' clock."
print(alphabet_position(text))
```
Результат:

```
20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11
```

---

## Другие решения:

```python
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
```
```python
def alphabet_position(text):
  al = 'abcdefghijklmnopqrstuvwxyz'
  return " ".join(filter(lambda a: a != '0', [str(al.find(c) + 1) for c in text.lower()]))
```
```python
import re

def alphabet_position(text):
    return " ".join([str(ord(i) - 96) for i in re.findall('[a-z]', text.lower())])
```
