## 5 Kyu - The Hashtag Generator
---
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples
```
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
```

---
Другое решение
```python
def generate_hashtag(s):
    hashtag = '#' + ''.join(word.capitalize() for word in s.split() if word)
    return hashtag if 0 < len(hashtag) <= 140 else False
```
Этот код делает то же самое, что и исходный код, но более компактно. Подробности:

Вместо отдельного условия проверки на пустую строку или строку, состоящую только из пробелов, используется проверка истинности (truthiness) значения переменной s в условии if.
Вместо цикла for используется генератор списка (list comprehension), который создает список слов, удовлетворяющих условию if.
Функция join объединяет отфильтрованные слова в единый строковый объект.
Выражение hashtag if 0 < len(hashtag) <= 140 else False использует тернарный оператор для возвращения хэштега, если его длина находится в допустимом диапазоне, или False в противном случае.