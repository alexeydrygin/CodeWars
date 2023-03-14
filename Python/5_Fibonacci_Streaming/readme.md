## 5 kyu - Fibonacci Streaming
[Ссылка на задачу](https://www.codewars.com/kata/55695bc4f75bbaea5100016b "Fibonacci Streaming")

You're going to provide a needy programmer a utility method that generates an infinite sized, sequential `IntStream` (in TypeScript and JavaScript `Iterator<number>`, in Python `generator`) which contains all the numbers in a fibonacci sequence.

Use `BigInt` in JS as numbers get too big for `Number`.

A fibonacci sequence starts with two `1`s. Every element afterwards is the sum of the two previous elements. See:

    1, 1, 2, 3, 5, 8, 13, ..., 89, 144, 233, 377, ...

---
## Задание:

## 5 kyu - потоковая передача Fibonacci
[SSSLKA na зadaчue] (https://www.codewars.com/kata/55695bc4f75bbaea5100016b "Fibonacci Streaming")

Вы собираетесь предоставить нуждающемуся программисту метод утилиты, который генерирует бесконечный, последовательный `intstream` (в TypeScript и JavaScript` iterator <cumber> `, в Python` Generator`), который содержит все числа в последовательности Fibonacci.

Используйте `bigint` в JS, так как цифры становятся слишком большими для` number`.

Последовательность Фибоначчи начинается с двух `1`.Каждый элемент впоследствии является суммой двух предыдущих элементов.Видеть:

    1, 1, 2, 3, 5, 8, 13, ..., 89, 144, 233, 377, ...

---

Данный код представляет собой функцию-генератор в языке программирования Python, которая создает бесконечный генератор целых чисел из последовательности чисел Фибоначчи.

Последовательность Фибоначчи начинается с двух чисел 1. Каждое последующее число равно сумме двух предыдущих чисел. Например, первые несколько чисел последовательности выглядят следующим образом: 1, 1, 2, 3, 5, 8, 13 и т.д.

Функция-генератор fib() начинает с генерации двух первых чисел последовательности, затем на каждой итерации вычисляет следующее число, как сумму двух предыдущих. Далее функция возвращает новое число и продолжает вычислять последующие числа при каждом новом вызове. Таким образом, можно использовать данную функцию-генератор для получения бесконечной последовательности чисел Фибоначчи.