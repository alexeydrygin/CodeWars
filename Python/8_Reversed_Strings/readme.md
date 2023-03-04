## Reversed Strings

---

Complete the solution so that it reverses the string passed into it.

```
'world'  =>  'dlrow'
'word'   =>  'drow'
```

---

## Вот один из способов перевернуть строку на Python:

```python

def reverse_string(s):
    return s[::-1]
```

В этом решении мы используем срезы для обращения строки. Синтаксис [::-1] создает новую строку, которая начинается с конца исходной строки и проходит до начала, беря каждый символ по пути.

Вот как вы можете использовать функцию для обращения примерных строк:

```python

print(reverse_string('world'))  # Вывод: 'dlrow'
print(reverse_string('word'))   # Вывод: 'drow'
```
