## Moving Zeros To The End

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements. pyton.

```
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
```

---

## Вот алгоритм на Python, который принимает массив и перемещает все нули в конец, сохраняя порядок других элементов:

---

Давайте разберем алгоритм по шагам:

- Подсчитываем количество нулей в массиве с помощью метода count() и сохраняем в переменную zero_count.

- Используем генератор списка для создания нового списка arr, который содержит только ненулевые элементы из исходного массива.

- Используем метод extend() для добавления zero_count нулей в конец arr.

- Возвращаем измененный список arr.

Вот пример использования этой функции:

```
code
>>> move_zeros([1, 0, 1, 2, 0, 1, 3])
[1, 1, 2, 1, 3, 0, 0]
```

---

## Варианты решений:

```
def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)
```

```
def move_zeros(array):
    return [x for x in array if x] + [0]*array.count(0)
```

```
def move_zeros(array):

    '''Returns an array of integers with the 0's at the end
       input: an array of integers
       output: an array of integers'''#

    for i in array: #traverse the array
        if i == 0: #checks if 'i' is equal to 0
            array.remove(0) #remove a 0 everytime we find one
            array.append(0) #appends a 0 everytime we find one
    return array #returns the updated array
```
