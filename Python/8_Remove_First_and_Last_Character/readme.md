## 8 kyu - Remove First and Last Character
[Ссылка на задачу](https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0 "Remove First and Last Character")

It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string.  You don't have to worry with strings with less than two characters.

---
## Задание:

## 8 kyu - удалить первый и последний персонаж
[SCSHLCA na зadaчue] (https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0 «Снимите первый и последний персонаж»)

Это довольно просто.Ваша цель - создать функцию, которая удаляет первые и последние символы строки.Вам дал один параметр, исходную строку.Вам не нужно беспокоиться с струнами с менее чем двумя персонажами.

---

Вы можете вызвать эту функцию и передать ей строку, из которой вы хотите удалить первый и последний символ, как аргумент. Например:

```python
original_string = "Hello, world!"
new_string = remove_first_last_characters(original_string)
print(new_string)
```
Обратите внимание, что функция использует срезы для удаления первого и последнего символа строки. Синтаксис [1:-1] означает, что нужно взять все символы строки, кроме первого и последнего.