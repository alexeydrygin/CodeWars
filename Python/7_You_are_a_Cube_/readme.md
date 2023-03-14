## 7 kyu - You are a Cube!
[Ссылка на задачу](https://www.codewars.com/kata/57da5365a82a1998440000a9 "You are a Cube!")

In geometry, a cube is a three-dimensional solid object bounded by six square faces, facets or sides, with three meeting at each vertex.The cube is the only regular hexahedron and is one of the five Platonic solids. It has 12 edges, 6 faces and 8 vertices.The cube is also a square parallelepiped, an equilateral cuboid and a right rhombohedron. It is a regular square prism in three orientations, and a trigonal trapezohedron in four orientations. 

You are given a task of finding a if the provided value is a perfect cube!  

---
## Задание:

## 7 kyu - ты куб!
[SSSLKA na зadaчue] (https://www.codewars.com/kata/57da5365a82a19984440000a9 "Вы - куб!")

В геометрии куб представляет собой трехмерный твердый объект, ограниченный шестью квадратными лицами, гранями или боками, с тремя встречами в каждой вершине. Куб является единственным обычным гексаэдром и является одним из пяти платонических веществ.Он имеет 12 краев, 6 грани и 8 вершин. Куб также представляет собой квадратный параллелепип, равенственный кубоид и правый ромбоэдрон.Это обычная квадратная призма в трех ориентациях, и тригональный трапецирдрон в четырех ориентациях.

Вам дается задача найти, если предоставленная стоимость является идеальным кубом!


---


Чтобы определить, является ли заданное значение идеальным кубом, можно взять кубический корень из этого значения и проверить, является ли результат целым числом. Если результат является целым числом, то заданное значение является идеальным кубом, в противном случае - нет.

Можно написать функцию на Python для реализации этого метода. Первым шагом в функции мы вычисляем кубический корень заданного значения n с помощью оператора возведения в степень **(1/3). Затем мы округляем результат с помощью функции round() для того, чтобы он был целым числом. Далее мы проверяем, равен ли куб округленного значения заданному значению n. Если да, то мы возвращаем True, что означает, что заданное значение является идеальным кубом, в противном случае мы возвращаем False.

Давайте протестируем эту функцию на нескольких примерах:

```python
print(isPerfectCube(27))    # Вывод: True
print(isPerfectCube(64))    # Вывод: True
print(isPerfectCube(125))   # Вывод: True
print(isPerfectCube(100))   # Вывод: False
print(isPerfectCube(150))   # Вывод: False
```
Функция правильно определяет идеальные кубы как True, а не-идеальные кубы как False.