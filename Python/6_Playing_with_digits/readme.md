## 6 Kyu - Playing with digits

---

ome numbers have funny properties. For example:

> 89 --> 8¹ + 9² = 89 \* 1

> 695 --> 6² + 9³ + 5⁴= 1390 = 695 \* 2

> 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 \* 51

Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p

- we want to find a positive integer k, if it exists, such that the sum of the digits of n taken to the successive powers of p is equal to k \* n.
  In other words:

> Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n \* k

If it is the case we will return k, if not return -1.

Note: n and p will always be given as strictly positive integers.

```
dig*pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
dig*pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
dig*pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
dig*pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
```

---

функция на языке Python, которая принимает два положительных целых числа n и p в качестве входных данных и возвращает положительное целое число k, если оно существует, такое что сумма цифр n, возведенных в последовательные степени p, равна k \* n, в противном случае она возвращает -1:

```python
def dig_pow(n, p):
    digits = [int(d) for d in str(n)]
    s = sum([d**(p+i) for i,d in enumerate(digits)])
    if s % n == 0:
        return s // n
    else:
        return -1
```

Вот как работает эта функция:

- digits = [int(d) for d in str(n)] создает список из цифр числа n.
- s = sum([d**(p+i) for i,d in enumerate(digits)]) вычисляет сумму цифр n, возведенных в последовательные степени p.
- if s % n == 0: проверяет, делится ли s на n.
- return s // n возвращает s деленное на n в качестве значения k, если оно существует.
  return -1 возвращает -1, если k не существует.
  Обратите внимание, что функция использует функцию enumerate, чтобы вычислить последовательные степени p для каждой цифры числа n.

Вот некоторые примеры использования функции:

```python
>>> dig_pow(89, 1)
1
>>> dig_pow(92, 1)
-1
>>> dig_pow(695, 2)
2
>>> dig_pow(46288, 3)
51
```

---

Другие решения:

```python
def dig_pow(n, p):
    k, fail = divmod(sum(int(d)**(p + i) for i, d in enumerate(str(n))), n)
    return -1 if fail else k
```

```python
dig_pow=lambda n,p:[-1 if sum([(int(str(n)[i]))**(p+i) for i in range (len(str(n)))])/n!=sum([(int(str(n)[i]))**(p+i) for i in range (len(str(n)))])//n else sum([(int(str(n)[i]))**(p+i) for i in range (len(str(n)))])//n][0]
```

```python
def dig_pow(n, p):
    ns = str(n)
    a = sum([int(ns[i]) ** (p + i) for i in range(len(ns))]) / n
    if a != int(a):
        return -1
    return a
```
