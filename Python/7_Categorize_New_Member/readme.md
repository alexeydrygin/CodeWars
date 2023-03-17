## 7 kyu - Categorize New Member
[Ссылка на задачу](https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa "Categorize New Member")

The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.
## Input

Input will consist of a list of pairs. Each pair contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.

## Output
Output will consist of a list of string values (in Haskell and C: `Open` or `Senior`) stating whether the respective member is to be placed in the senior or open category.

### Example

```
input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]
```


---
## Задание:

## 7 kyu - классифицировать новый участник
[SSSLKA na зadaчue](https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa "Категоризируйте новый участник")

В Croquet Club Western Suburbs есть две категории членства, старшие и открытые.Они хотели бы вашей помощи в форме заявки, которая сообщит потенциальным участникам, какую категорию они будут размещены.

Чтобы стать старшим, члену должно быть не менее 55 лет и иметь гандикап более 7. В этом кроке -клубе гандикапы варьируются от -2 до +26;Чем лучше игрок, тем ниже гандикап.
## Вход

Ввод будет состоять из списка пар.Каждая пара содержит информацию для одного потенциального члена.Информация состоит из целого числа возраста человека и целого числа для гандикапа человека.

## Выход
Вывод будет состоять из списка строковых значений (в Haskell и C: `open` или` Senior`), в котором говорится, должен ли соответствующий участник быть помещен в категорию старшего или открытого.

### Пример

```
Вход = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]]
output = [«open», «open», «старший», «open», «open», «Старший»]
```

---

Функция categorize_members принимает список пар, где каждая пара представляет возраст и гандикап участника. Затем она проходит по каждому участнику и проверяет, соответствует ли он критериям для категории "Senior", как указано в условии задачи. Если участник соответствует критериям, функция добавляет строку "Senior" в итоговый список, в противном случае добавляет "Open". Наконец, функция возвращает итоговый список.

Вы можете вызвать эту функцию с предоставленным списком входных данных, чтобы получить желаемый результат:

```python
input = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = categorize_members(input)
print(output)
```
Это должно вывести:

```python
["Open", "Open", "Senior", "Open", "Open", "Senior"]
```