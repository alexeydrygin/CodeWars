## 5 Kyu - Find Out the Number of Gold Coins!
---
Напишите функцию number_of_coins, которая возвращает минимальное количество золотых монет в сундуке, основываясь на подсказках стража. Функция принимает информацию в виде списка кортежей:

[(a1, m1), (a2, m2), ... , (aN, mN)]

Например:

Предположим, что подсказки стража выглядят следующим образом:

Если бы количество монет было поделено между 2 людьми, то был бы 1 остаток монеты.

Если бы количество монет было поделено между 5 людьми, то было бы 2 остатка монет.

Таким образом, минимальное количество золотых монет равно 7, потому что 7 - это наименьшее число, которое при делении на 2 имеет остаток 1 и при делении на 5 имеет остаток 2. Таким образом:

number_of_coins([(1, 2), (2, 5)]) = 7

---

Here's the implementation of the number_of_coins() function that uses the Chinese Remainder Theorem to find the smallest number that satisfies the given remainders:

```python

def number_of_coins(info):
    # Calculate the product of all moduli
    m = 1
    for _, mod in info:
        m *= mod

    # Calculate the sum of all residues
    x = 0
    for a, mod in info:
        b = m // mod
        x += a * b * pow(b, -1, mod)

    return x % m
```

Here's how the function works:

First, we calculate the product of all the moduli given in the input. This is done using a loop that iterates over all the tuples in the input list and multiplies the second element of each tuple with the current value of m.

Next, we calculate the sum of all the residues. This is done using another loop that iterates over all the tuples in the input list. For each tuple, we calculate b = m // mod, which is the product of all the moduli except the current modulus. Then we calculate a * b * pow(b, -1, mod), which is the residue for the current modulus. We add all the residues to get the final value of x.

Finally, we return the smallest non-negative integer that is congruent to x modulo m. This is done by calculating x % m.

Note that we use the pow() function with the third argument to calculate the modular inverse of b modulo mod.