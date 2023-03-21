## 8 kyu - Reversed sequence 
[Ссылка на задачу](https://www.codewars.com/kata/5a00e05cc374cb34d100000d "Reversed sequence ")

Build a function that returns an array of integers from n to 1 where ```n>0```.

Example : `n=5` --> `[5,4,3,2,1]`

~~~if:nasm
*NOTE: In NASM, the function signature is* `int *reverse_seq(int n, size_t *size)` *where the first parameter* `n` *is as described above and the second parameter* `size` *is a pointer to an "out" parameter which should be set to the size of the array your function returns (which should be equal to* `n` *if your implementation is correct).*
~~~

~~~if:riscv
RISC-V: The function signature is

```c
void n_to_1(int n, int *arr);
```

Write your result to `arr`. You may assume it is large enough to hold the result. You do not need to return anything.
~~~

---
## Задание:

## 8 kyu - обратная последовательность
[SSSLKA na зadaчue] (https://www.codewars.com/kata/5a00e05cc374cb34d100000d «перевернутая последовательность»)

Создайте функцию, которая возвращает массив целых чисел от N до 1, где ```n> 0``.

Пример: `n = 5` ->` [5,4,3,2,1] `

~~~ if: nasm
*Примечание: в NASM подпись функции - *`int *reample_seq (int n, size_t *size)` *Где первый параметр *`n` *, как описано выше, и второй параметр *` size` * - указатель.к параметру «Out», который должен быть установлен на размер массива, который возвращает ваша функция (что должно быть равным* `n`*, если ваша реализация верна).*
~~~

~~~ if: RISCV
RISC-V: подпись функции

`` c
void n_to_1 (int n, int *arr);
```

Напишите свой результат на `arr '.Вы можете предположить, что он достаточно большой, чтобы удерживать результат.Вам не нужно ничего возвращать.
~~~

---

Функция range() используется для создания последовательности целых чисел от n до 1 с шагом -1 (т.е. в обратном порядке). Затем функция list() используется для преобразования этой последовательности в список целых чисел.

Вы можете вызвать эту функцию с значением n, большим нуля, чтобы получить нужный результат:

```python

>>> countdown(5)
[5, 4, 3, 2, 1]
```
Эта функция будет работать для любого положительного целого значения n.

---

```python
def reverse_seq(n):
    output = []
    for i in range(n):
        output.append(n)
        n -= 1
    return output
```
```python
reverse_seq = lambda n: list(range(n, 0, -1)
```
