## 8 Kyu - How good are you really?

---

There was a test in your class and you passed it. Congratulations!
But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return True if you're better, else False!

Note:
Your points are not included in the array of your class's points. For calculating the average point you may add your point to the given array!

---

В вашем классе был тест, и вы его сдали. Поздравляю!
Но вы амбициозный человек. Вы хотите знать, лучше ли вы, чем средний ученик в вашем классе.

Вы получаете массив с результатами тестов ваших сверстников. Теперь рассчитайте среднее значение и сравните свой результат!

Верните True, если вы лучше, в противном случае False!

Примечание:
Ваши баллы не включены в массив баллов вашего класса. Для вычисления среднего балла вы можете добавить свой балл в данный массив!

---

Здесь функция better_than_average принимает два аргумента: class_points, массив с результатами тестов ваших сверстников, и your_points, ваш результат теста. Функция добавляет ваш результат в массив баллов класса, затем вычисляет средний балл класса и сравнивает его со своим результатом. Если ваш результат выше среднего балла класса, функция возвращает True, в противном случае - False.

Пример использования:

```python

class_points = [85, 90, 92, 75, 88]
your_points = 86

print(better_than_average(class_points, your_points))  # True
```

Здесь средний балл класса равен (85 + 90 + 92 + 75 + 88 + 86) / 6 = 85.33. Таким образом, ваш балл 86 выше среднего балла класса, и функция возвращает True.

---

## Другие решения

```python
better_than_average = lambda a,b:(sum(a)/len(a))<b
```

```python
def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)
```

```python
def better_than_average(class_points, your_points):
    mean = sum(class_points) / len(class_points)
    print(mean)
    if mean > your_points:
        return False
    else:
        return True
```
