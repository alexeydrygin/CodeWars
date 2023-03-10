## 7 Kyu - Friend or Foe?

---

Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

i.e.

```
friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
```

Note: keep the original order of the names in the output.

---

## Создайте программу, которая фильтрует список строк и возвращает список, в котором есть только имя вашего друга.

Если в имени ровно 4 буквы, вы можете быть уверены, что это должен быть ваш друг! В противном случае, вы можете быть уверены, что это не так...

Пример: Ввод = ["Райан", "Киран", "Джейсон", "Ты"], Вывод = ["Райан", "Ты"]

т.е.

друг ["Райан", "Киран", "Марк"] "должен быть` ["Райан", "Марк"]
Примечание: сохраните первоначальный порядок имен в выходных данных.

---

Эта функция принимает список имен names и возвращает список имен друзей, т.е. имена, которые состоят из ровно 4 букв.

Мы создаем пустой список friends, затем итерируемся по списку имен names. Если длина имени равна 4, мы добавляем его в список friends. В конце функции мы возвращаем список друзей.

Пример использования функции:

```python

names = ["Ryan", "Kieran", "Jason", "Yous"]
friend_names = friend(names)
print(friend_names)  # Output: ["Ryan", "Yous"]
```

Здесь мы передаем список имен names в функцию friend, получаем список друзей friend_names и выводим его на экран.

## Другие решения

```python
def friend(x):
    return [f for f in x if len(f) == 4]
```

```python
def friend(x):
    return filter(lambda name: len(name) == 4, x)
```
