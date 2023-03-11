## 7 Kyu - Find the next perfect square
---
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.

Examples:(Input --> Output)
```
121 --> 144
625 --> 676
114 --> -1 since 114 is not a perfect square
```

---
## Метод findNextSquare на языке Python, который находит следующее целочисленное квадратное число после заданного параметра:

Метод использует библиотеку math, чтобы вычислить квадратный корень из sq и проверить, является ли он целым числом. Если да, то метод вычисляет следующее квадратное число, добавляя 1 к квадратному корню и возводя результат в квадрат. Если квадратный корень не является целым числом, метод возвращает -1.

Вот несколько примеров использования метода findNextSquare:

```python
print(findNextSquare(121)) # Output: 144
print(findNextSquare(625)) # Output: 676
print(findNextSquare(114)) # Output: -1
```
Другие решения:

```python
def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1
```
```python
def find_next_square(sq):
    x = sq**0.5    
    return -1 if x % 1 else (x+1)**2
```
```python
def find_next_square(sq):
    return (sq**.5+1)**2 if (sq**.5)%1==0.0 else -1
```
