## 8 kyu - Remove String Spaces
[Ссылка на задачу](https://www.codewars.com/kata/57eae20f5500ad98e50002c5 "Remove String Spaces")

Write a function that removes the spaces from the string, then return the resultant string.

Examples:
```
Input -> Output
"8 j 8   mBliB8g  imjB8B8  jl  B" -> "8j8mBliB8gimjB8B8jlB"
"8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd" -> "88Bifk8hB8BB8BBBB888chl8BhBfd"
"8aaaaa dddd r     " -> "8aaaaaddddr"
```

~~~if:bf
The input string will be terminated with a null character `\0`.
~~~
~~~if:c,nasm
For C and Nasm, you must return a new dynamically allocated string.
~~~


---
## Задание:

## 8 kyu - удалить строковые пространства
[Ssslecka na зadaчue] (https://www.codewars.com/kata/57eae20f5500ad98e50002c5 "Снимите строковые пространства")

Напишите функцию, которая удаляет пространства из строки, затем верните результирующую строку.

Примеры:
```
Вход -> Выход
"8 J 8 MBLIB8G IMJB8B8 JL B" -> "8J8MBLIB8GIMJB8B8JLB"
"8 8 Bi Fk8h B 8 BB8B B B B888 C HL8 BHB FD" -> "88BIFK8HB8BB8BBB888CHL8BHBFD"
"8AAAAA DDDD R" -> "8AAAAADDDDR"
```

~~~ if: bf
Входная строка будет завершена с помощью нулевого символа `\ 0`.
~~~
~~~ if: c, nasm
Для C и NASM вы должны вернуть новую динамически выделенную строку.
~~~

---

Эта функция использует метод replace() для замены пробелов во входной строке на пустую строку. Затем результат возвращается.

Примеры использования:

```python
print(no_space("8 j 8   mBliB8g  imjB8B8  jl  B"))  # "8j8mBliB8gimjB8B8jlB"
print(no_space("8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd"))  # "88Bifk8hB8BB8BBBB888chl8BhBfd"
print(no_space("8aaaaa dddd r     "))  # "8aaaaaddddr"
```

## Варианты

```
def no_space(x):
    return "".join(x.split())
```

```
def no_space(x):
    return ''.join([s for s in x if not s.isspace()])
```