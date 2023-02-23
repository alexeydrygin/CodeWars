## Take a Ten Minutes Walk

You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

> Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).

## Код на Python, который проверяет, займет ли прогулка 10 минут, и вернет True, если также ведет обратно к точке старта. В противном случае функция вернет False.

---

Как это работает:

- Если длина прогулки не равна 10, функция возвращает False.
- Если длина прогулки равна 10, мы начинаем с начальной точки (координаты (0, 0)) и перемещаемся в соответствии с указанными направлениями. Каждое направление изменяет координаты на единицу в соответствующем направлении (север увеличивает y, юг уменьшает y, восток увеличивает x, запад уменьшает x).
- После того, как мы прошли по всей прогулке, мы проверяем, вернулись ли мы на место (т.е. координаты равны (0, 0)). Если да, возвращаем True, в противном случае - False.

## Варианты:

```
def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
```

```
def isValidWalk(walk):
    if (walk.count('n') == walk.count('s') and
        walk.count('e') == walk.count('w') and
        len(walk) == 10):
            return True
    return False
```
