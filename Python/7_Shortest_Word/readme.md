## Shortest Word

Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

## найти длину самого короткого слова

Для решения этой задачи нужно разбить строку на слова и найти длину самого короткого слова. Это можно сделать следующим образом:

Разбить строку на слова, используя метод split.
Инициализировать переменную shortest_length длиной первого слова.
Проходить по всем словам, начиная со второго, и сравнивать их длину с shortest_length. Если длина слова меньше shortest_length, то обновлять значение shortest_length.
После прохода по всем словам вернуть shortest_length.

## Варианты:

```python
def find_short(s):
    return min(len(x) for x in s.split())
```

```python
def find_short(s):
    return min(map(len, s.split(' ')))
```
