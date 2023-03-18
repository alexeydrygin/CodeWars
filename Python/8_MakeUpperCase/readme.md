## 8 kyu - MakeUpperCase
[Ссылка на задачу](https://www.codewars.com/kata/57a0556c7cb1f31ab3000ad7 "MakeUpperCase")

Write a function which converts the input string to uppercase.

~~~if:bf
For BF all inputs end with \0, all inputs are lowercases and there is no space between.
~~~

~~~if:riscv
RISC-V: The function signature is

```c
void to_upper_case(const char *str, char *out);
```

`str` is the input string. Write your result to `out`. You may assume it is large enough to hold the result. You do not need to return anything.
~~~


---
## Задание:

## 8 kyu - makeppercase
[Ssslecka na зadaчue] (https://www.codewars.com/kata/57a0556c7cb1f31ab3000ad7 "makeuppercase")

Напишите функцию, которая преобразует входную строку в верхний регистр.

~~~ if: bf
Для BF все входы заканчиваются \ 0, все входы имеют более низкие точки, и между ними нет места.
~~~

~~~ if: RISCV
RISC-V: подпись функции

`` c
void to_upper_case (const char *str, char *out);
```

`str` - входная строка.Напишите свой результат, чтобы «Out».Вы можете предположить, что он достаточно большой, чтобы удерживать результат.Вам не нужно ничего возвращать.
~~~

---

You can call this function and pass the string that you want to convert to uppercase as an argument. For example:

```python
input_string = "Hello, world!"
upper_string = to_uppercase(input_string)
print(upper_string)
```
This will output:

```
HELLO, WORLD!
```