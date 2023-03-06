## Digit^2

---

Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

Note: The function accepts an integer and returns an integer.

## Happy Coding!

---

Функция, которая возводит в квадрат каждую цифру числа и объединяет их.

## Другие решения:

```python
def square_digits(x):
    return int("".join(str(int(i)*int(i)) for i in str(x)))
```

```python
def square_digits(num):
    new_list = []
    for i in str(num):
        new_list.append(str(int(i)**2))
    return(int("".join(new_list)))
    #x = str(num).split()
    #sliced = x[::]
    #return(sliced)
```
