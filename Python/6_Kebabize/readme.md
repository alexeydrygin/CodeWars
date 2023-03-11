## 6 Kyu - Kebabize

---

Modify the kebabize function so that it converts a camel case string into a kebab case.

```
"camelsHaveThreeHumps"  -->  "camels-have-three-humps"
"camelsHave3Humps"  -->  "camels-have-humps"
"CAMEL"  -->  "c-a-m-e-l"
```

Notes:

- the returned string should only contain lowercase letters

---

**Функция на языке Python, которая принимает строку в формате camel case и возвращает строку в формате kebab case:**

```python
def kebabize(string):
    # удаляем все цифры из строки
    string = ''.join(c for c in string if not c.isdigit())
    # добавляем '-' перед каждой заглавной буквой, кроме первой
    string = ''.join('-' + c.lower() if c.isupper() and i != 0 else c.lower() for i, c in enumerate(string))
    # удаляем первый символ, если он является '-'
    if string and string[0] == '-':
        string = string[1:]
    return string
```

Вот как работает эта функция:

- string = ''.join(c for c in string if not c.isdigit()) удаляет все цифры из строки, чтобы строка содержала только буквы.
- string = ''.join('-' + c.lower() if c.isupper() and i != 0 else c.lower() for i, c in enumerate(string)) добавляет символ '-' перед каждой заглавной буквой, кроме первой, и преобразует все буквы в нижний регистр.
- if string and string[0] == '-': string = string[1:] удаляет первый символ '-' из строки, если он существует.

Обратите внимание, что функция использует методы isupper() и isdigit() для проверки, является ли каждый символ заглавной буквой или цифрой соответственно, а также функцию enumerate(), чтобы получить индекс каждого символа в строке.

Вот некоторые примеры использования функции:

```python

>>> kebabize("camelsHaveThreeHumps")
'camels-have-three-humps'
>>> kebabize("camelsHave3Humps")
'camels-have-humps'
>>> kebabize("CAMEL")
'c-a-m-e-l'
```

## Другие решения:

```python
def kebabize(s):
    return ''.join(c if c.islower() else '-' + c.lower() for c in s if c.isalpha()).strip('-')
```

```python
def kebabize(string):
    res = ''
    for i in string:
        if i.isalpha():
            if i.isupper():
                res += '-' + i
            else:
                res += i
    return res.strip('-').lower()
```

```python
def kebabize(s): import re; s = re.sub('\d', '', s); return re.sub('(?<!^)(?=[A-Z])', '-', s).lower()
```
