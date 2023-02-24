## Pair of gloves

Winter is coming, you must prepare your ski holidays. The objective of this kata is to determine the number of pair of gloves you can constitute from the gloves you have in your drawer.

Given an array describing the color of each glove, return the number of pairs you can constitute, assuming that only gloves of the same color can form pairs.

Examples:

```python
input = ["red", "green", "red", "blue", "blue"]
result = 2 (1 red pair + 1 blue pair)

input = ["red", "red", "red", "red", "red", "red"]
result = 3 (3 red pairs)
```

### Функции на Python, которая принимает список цветов перчаток и возвращает количество пар, которые можно составить, предполагая, что только перчатки одного цвета могут составлять пары

Функция использует словарь, чтобы подсчитать количество перчаток каждого цвета в списке. Затем мы проходим по значениям словаря (то есть по количеству перчаток каждого цвета) и добавляем количество пар, которые можно составить для каждого цвета, к общему количеству пар. Обратите внимание, что мы используем оператор "//" для деления, чтобы получить только целочисленную часть результата.

Вот примеры использования:

```python
gloves1 = ["red", "green", "red", "blue", "blue"]
print(count_pairs(gloves1))  # Output: 2

gloves2 = ["red", "red", "red", "red", "red", "red"]
print(count_pairs(gloves2))  # Output: 3
```

В первом примере у нас есть 2 красных перчатки и 2 синих перчатки, поэтому мы можем составить по одной паре для каждого цвета. Во втором примере у нас есть только красные перчатки, поэтому мы можем составить три пары.

---

Иные решения:

```python
def number_of_pairs(gloves):
    return sum(gloves.count(color)//2 for color in set(gloves))
```
