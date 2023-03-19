## 6 kyu - Build Tower
[Ссылка на задачу](https://www.codewars.com/kata/576757b1df89ecf5bd00073b "Build Tower")

Build Tower
---

Build a pyramid-shaped tower, as an array/list of strings, given a positive integer `number of floors`. A tower block is represented with `"*"` character.

For example, a tower with `3` floors looks like this:

```
[
  "  *  ",
  " *** ", 
  "*****"
]
```

And a tower with `6` floors looks like this:

```
[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]
```

___

Go challenge [Build Tower Advanced](httpss://www.codewars.com/kata/57675f3dedc6f728ee000256) once you have finished this :)


---
## Задание:

## 6 kyu - Build Tower
[SSSLKA na зadaчue] (https://www.codewars.com/kata/576757b1df89ecf5bd00073b "Строительная башня")

Построить башню
---

Создайте башню в форме пирамиды в виде массива/списка строк, учитывая положительное целое число «количество полов».Блок башни представлен с `"*"` necument.

Например, башня с `3` Похоже выглядит так:

```
[
  " *",
  "***",
  "*****"
]
```

И башня с `6` Похоже выглядит так:

```
[
  " *",
  "***",
  "*****",
  "*******",
  "*********",
  "***********
]
```

___

Go Challenge [Build Tower Advanced] (httpss: //www.codewars.com/kata/57675f3dedc6f728ee000256), как только вы закончите это :)

---

Для решения задачи нужно создать список, в котором каждый элемент представляет собой строку, содержащую "*" и пробелы. Количество символов в строке должно быть не меньше, чем 2 * n - 1, где n - это количество этажей. Количество пробелов в начале строки равно n - 1, и оно уменьшается на 1 для каждой следующей строки. Количество звездочек в строке равно 2 * i + 1, где i - это номер строки (начиная с 0).

---

```python
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
```
```python
def tower_builder(n_floors):
    # build here
    tower = []
    for i in range(n_floors):
       tower.append(' '*(n_floors-i-1) + '*'*(2*i+1) + ' '*(n_floors-i-1))
    return tower
```
```python
tower_builder=lambda n:[str.center('*'*i,n*2-1)for i in range(1,n*2,2)]
```
