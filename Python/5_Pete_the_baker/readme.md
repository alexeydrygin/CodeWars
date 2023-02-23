### Pete, the baker

Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function `cakes()`, which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

> Пит любит печь торты. У него есть рецепты и ингредиенты. К сожалению, он не силен в математике. Поможешь ему узнать, сколько тортов он сможет испечь, учитывая его рецепты?

> Напишите функцию `cakes()`, которая принимает рецепт (объект) и доступные ингредиенты (тоже объект) и возвращает максимальное количество тортов, которые Пит может испечь (целое число). Для простоты нет единиц измерения количества (например, 1 фунт муки или 200 г сахара — это просто 1 или 200). Ингредиенты, отсутствующие в объектах, можно считать равными 0.

Examples:

```
# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
```

### Вот решение задачи на Python, которое поможет Питу определить, сколько пирогов он может испечь на основе своих рецептов и имеющихся ингредиентов

---

Алгоритм решения следующий:

- Создаем список ratios, в который будем добавлять результаты деления имеющегося количества ингредиентов на требуемое для каждого ингредиента из рецепта.
- Проходимся по всем ингредиентам, необходимым для рецепта, и проверяем, есть ли они в имеющихся ингредиентах. Если какого-то ингредиента не хватает, возвращаем 0.
- Если все ингредиенты из рецепта есть в имеющихся ингредиентах, то добавляем результат деления имеющегося количества ингредиента на требуемое в список ratios.
- Возвращаем минимальное значение в списке ratios - это и будет определять, сколько пирогов можно испечь на основе имеющихся ингредиентов.
  Пример использования функции:

```
recipe = {'flour': 500, 'sugar': 200, 'eggs': 1}
available = {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}
cakes(recipe, available)
2
```

> В данном случае Пит может испечь только 2 пирога, так как количество муки и сахара позволяет испечь только два пирога, а яиц достаточно для пяти. Молока нет в рецепте, поэтому его наличие не учитывается.

---

# Варианты:

```
def cakes(recipe, available):
	return min(available.get(k, 0)/recipe[k] for k in recipe)
```

```
def cakes(recipe, available):
    try:
        return min([available[a]/recipe[a] for a in recipe])
    except:
        return 0
```

```
def cakes(recipe, ingredients):
    return min(ingredients.get(k, 0) / v for k, v in recipe.iteritems())
```
