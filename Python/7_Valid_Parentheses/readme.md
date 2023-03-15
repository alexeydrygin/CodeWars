## 7 kyu - Valid Parentheses
[Ссылка на задачу](https://www.codewars.com/kata/6411b91a5e71b915d237332d "Valid Parentheses")

***BETA NOTE:***

This kata is intended as a rework for [this existing kata](httpss://www.codewars.com/kata/52774a314c2333f0a7000688), which is to be eventually retired. See [this thread](httpss://github.com/codewars/content-issues/issues/180) for context. The intent of the re-make is to completely overhaul the tests, as well as allowing for a much more appropriate rank (~7kyu). Translations are gladly welcomed!

---

Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return `true` if the string is valid, and `false` if it's invalid.

## Examples

```
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
```

## Constraints

`0 <= length of input <= 100`

- All inputs will be strings, consisting only of characters `(` and `)`.
- Empty strings are considered balanced (and therefore valid), and will be tested.
- For languages with mutable strings, the inputs should not be mutated.

<br>

***Protip:** If you are trying to figure out why a string of parentheses is invalid, paste the parentheses into the code editor, and let the code highlighting show you!*

---
## Задание:

## 7 kyu - Действительные скобки
[SSSLKA na зadaчue] (https://www.codewars.com/kata/6411b91a5e71b915d237332d «Допустимые скобки»)

*** Бета -примечание: ***

Эта Kata предназначена как переделка для [существующей kata] (httpss: //www.codewars.com/kata/52774a314c2333f0a7000688), который в конечном итоге должен быть вышел на пенсию.См.Цель повторного производства состоит в том, чтобы полностью пересмотреть тесты, а также обеспечить гораздо более подходящий ранг (~ 7KYU).Переводы с радостью приветствуются!

---

Напишите функцию, которая принимает строку скобок, и определяет, является ли порядок скобок действительными.Функция должна вернуть `true`, если строка действительна, и` false`, если она недействительна.

## Примеры

```
"()" => true
") ((()))" => false
"(" => ложный
"(()) ((() () ()) ())" => true
```

## ограничения

`0 <= длина ввода <= 100`

- Все входы будут строками, состоящими только из символов `(` и `)`.
- Пустые строки считаются сбалансированными (и, следовательно, действительными) и будут проверены.
- Для языков с изменчивыми строками входные данные не должны быть мутированы.

<br>

*** protip: ** Если вы пытаетесь выяснить, почему строка скобок недействительна, вставьте скобки в редактор кода и позвольте подсвещенному коду показать вам!*********

---

Эта функция на Python проверяет, правильно ли расставлены скобки в строке. Если скобки расставлены правильно, то функция возвращает True, иначе - False.

Вот как работает функция:

Создаём пустой стек.
Итерируемся по каждому символу во входной строке.
Если символ - открывающая скобка, то добавляем её в стек.
Если символ - закрывающая скобка, то проверяем, пуст ли стек. Если стек пуст, то возвращаем False, так как нет открывающей скобки, соответствующей закрывающей. Иначе, удаляем открывающую скобку из стека, чтобы соответствовать закрывающей скобке.
В конце итерации, если стек пуст, то все открывающие скобки были сопоставлены закрывающим скобкам и входная строка правильная. В противном случае, в стеке остаются открывающие скобки, которые не были сопоставлены закрывающим скобкам, и входная строка неправильная.
Для проверки функции можно вызвать её с различными входными строками:

```python
print(valid_parentheses("()"))  # True
print(valid_parentheses("())"))  # False
print(valid_parentheses("(()"))  # False
print(valid_parentheses("(())((()())())"))  # True
print(valid_parentheses(""))  # True
```

## Другие решения:

```python
def valid_parentheses(array):
    count = 0
    for item in array:
        if item == '(':
            count += 1
        elif count:
            count -= 1
        else:
            return False
    return count == 0
```
```python
def valid_parentheses(s):
    while '()' in s: s = s.replace('()', '')
    return len(s) == 0
```
```python
def valid_parentheses(paren_str):
    try:
        eval(f"lambda: {paren_str or ...}")
        return True
    except:
        return False
```
