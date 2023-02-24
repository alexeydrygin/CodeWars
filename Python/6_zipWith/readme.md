## zipWith

Task
zipWith ( or zip_with ) takes a function and two arrays and zips the arrays together, applying the function to every pair of values.
The function value is one new array.

If the arrays are of unequal length, the output will only be as long as the shorter one.
(Values of the longer array are simply not used.)

Inputs should not be modified.

Examples

```
zip_with( pow, [10,10,10,10], [0,1,2,3] )     =>  [1,10,100,1000]
zip_with( max, [1,4,7,1,4,7], [4,7,1,4,7,1])  =>  [4,7,7,4,7,7]

def add(a,b): return a+b; # or from operator import add
zip_with( add,             [0,1,2,3], [0,1,2,3] )  =>  [0,2,4,6]  # Both forms are valid
zip_with( lambda a,b: a+b, [0,1,2,3], [0,1,2,3] )  =>  [0,2,4,6]  # Both are functions
```

Input validation
Assume all input is valid.

##

Реализуйте функцию zip_with, которая принимает на вход функцию и два массива и сопоставляет их друг с другом, применяя функцию ко всем парам значений. В результате должен получиться новый массив.

Если массивы разной длины, то в итоговый массив попадут только значения из более короткого массива. Значения из более длинного массива не используются.

Примеры:

```
zip_with(pow, [10,10,10,10], [0,1,2,3]) => [1,10,100,1000]
zip_with(max, [1,4,7,1,4,7], [4,7,1,4,7,1]) => [4,7,7,4,7,7]
zip_with(lambda a,b: a+b, [0,1,2,3], [0,1,2,3]) => [0,2,4,6]
```

Функции, передаваемые в zip_with, должны принимать два аргумента и возвращать одно значение. Все входные данные считайте корректными.

Конечный код функции zip_with

Он использует функцию zip, которая объединяет элементы двух списков в кортежи и возвращает итератор по ним. Затем мы проходим по этому итератору и применяем функцию fn к каждой паре элементов, используя генератор списка. Конечный результат - список значений, полученных применением функции fn к соответствующим парам элементов.

## варианты

```
def zip_with(a,b,c):
    return list(map(a,b,c))
```
