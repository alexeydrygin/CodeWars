## Best Travel

John and Mary want to travel between a few towns A, B, C ... Mary has on a sheet of paper a list of distances between these towns. ls = [50, 55, 57, 58, 60]. John is tired of driving and he says to Mary that he doesn't want to drive more than t = 174 miles and he will visit only 3 towns.

Which distances, hence which towns, they will choose so that the sum of the distances is the biggest possible to please Mary and John?

Example:
With list ls and 3 towns to visit they can make a choice between: [50,55,57],[50,55,58],[50,55,60],[50,57,58],[50,57,60],[50,58,60],[55,57,58],[55,57,60],[55,58,60],[57,58,60].

The sums of distances are then: 162, 163, 165, 165, 167, 168, 170, 172, 173, 175.

The biggest possible sum taking a limit of 174 into account is then 173 and the distances of the 3 corresponding towns is [55, 58, 60].

The function chooseBestSum (or choose_best_sum or ... depending on the language) will take as parameters t (maximum sum of distances, integer >= 0), k (number of towns to visit, k >= 1) and ls (list of distances, all distances are positive or zero integers and this list has at least one element). The function returns the "best" sum ie the biggest possible sum of k distances less than or equal to the given limit t, if that sum exists, or otherwise nil, null, None, Nothing, depending on the language. In that case with C, C++, D, Dart, Fortran, F#, Go, Julia, Kotlin, Nim, OCaml, Pascal, Perl, PowerShell, Reason, Rust, Scala, Shell, Swift return -1.

Examples:
ts = [50, 55, 56, 57, 58] choose_best_sum(163, 3, ts) -> 163

xs = [50] choose_best_sum(163, 3, xs) -> nil (or null or ... or -1 (C++, C, D, Rust, Swift, Go, ...)

ys = [91, 74, 73, 85, 73, 81, 87] choose_best_sum(230, 3, ys) -> 228

Notes:
try not to modify the input list of distances ls
in some languages this "list" is in fact a string (see the Sample Tests).

---

Джон и Мэри хотят путешествовать между несколькими городами A, B, C... У Мэри есть на листе бумаги список расстояний между этими городами. ls = [50, 55, 57, 58, 60]. Джону надоело водить машину, и он говорит Мэри, что не хочет проезжать больше t = 174 миль и посетит только 3 города.

Какие расстояния, следовательно, какие города они выберут, чтобы сумма расстояний была максимально возможной, чтобы угодить Мэри и Джону?

Пример:
Имея список ls и 3 города для посещения, они могут сделать выбор между: [50,55,57],[50,55,58],[50,55,60],[50,57,58],[50,57,60],[50,58,60],[55,57,58],[55,57,60],[55,58,60],[57,58,60].

Суммы расстояний тогда равны: 162, 163, 165, 165, 167, 168, 170, 172, 173, 175.

Наибольшая возможная сумма, учитывающая ограничение в 174, тогда равна 173, а расстояния до 3 соответствующих городов равны [55, 58, 60].

Функция chooseBestSum (или choose_best_sum или ... в зависимости от языка) примет в качестве параметров t (максимальная сумма расстояний, целое число >= 0), k (количество городов для посещения, k >= 1) и ls (список расстояний, все расстояния являются целыми положительными или нулевыми числами, и этот список содержит по крайней мере один элемент). Функция возвращает "наилучшую" сумму, то есть максимально возможную сумму k расстояний, меньшую или равную заданному пределу t, если эта сумма существует, или в противном случае nil, null, None, Nothing, в зависимости от языка. В этом случае с C, C++, D, Dart, Fortran, F#, Go, Julia, Kotlin, Nim, OCaml, Pascal, Perl, PowerShell, Reason, Rust, Scala, Shell, Swift возвращается значение -1.

Примеры:
тс = [50, 55, 56, 57, 58] выбираем*большую*сумму(163, 3, ts) -> 163

xs = [50] choose_best_sum(163, 3, xs) -> nil (или null, или ... или -1 (C++, C, D, Rust, Swift, Go, ...)

ys = [91, 74, 73, 85, 73, 81, 87] выбираем*большую*сумму(230, 3, ys) -> 228

Записи:
старайтесь не изменять входной список расстояний ls
в некоторых языках этот "список" на самом деле является строкой (см. Примеры тестов).

---

---

Чтобы решить эту проблему, мы можем использовать рекурсивный подход для генерации всех возможных комбинаций из k городов и вычисления суммы расстояний для каждой комбинации. Мы можем отслеживать максимальную сумму, которая меньше или равна заданному пределу t, и возвращать ее в качестве результата.

Функция choose_best_sum принимает три параметра: t, k и ls. t - максимальная сумма расстояний, которые Джон готов проехать, k - количество городов, которые Джон и Мэри хотят посетить, а ls - список расстояний между городами.

Функция определяет вложенную функцию find_best_sum, которая принимает три параметра: curr_sum, num_towns_visited и curr_index. curr_sum - это сумма расстояний для текущей комбинации городов, num_towns_visited - это количество городов, посещенных на данный момент, а curr_index - это индекс текущего города в списке ls.

Базовый случай рекурсии - это когда num_towns_visited равно k или когда curr_index равен длине списка ls. Если num_towns_visited равно k, мы проверяем, меньше ли curr_sum или равно t. Если это так, мы возвращаем curr_sum. Если оно больше t, мы возвращаем отрицательную бесконечность, потому что эта комбинация недопустима. Если curr_index равен длине списка ls, мы возвращаем отрицательную бесконечность, потому что городов для посещения больше нет.

Рекурсивный случай предполагает два варианта: включение текущего города в комбинацию или исключение его. Если мы включаем текущий город, мы вызываем find_best_sum с curr_sum + ls[curr_index], num_towns_visited + 1 и curr_index + 1. Если мы исключаем текущий город, мы вызываем find_best_sum с curr_sum, num_towns_visited и curr_index + 1. В результате мы возвращаем максимальное из этих двух значений.

Наконец, мы вызываем find_best_sum с начальными значениями curr_sum = 0, num_towns_visited = 0 и curr_index = 0, чтобы запустить рекурсию. Мы проверяем, равен ли результат отрицательной бесконечности, что означает, что не было найдено ни одной допустимой комбинации. Если это так, мы возвращаем None. В противном случае мы возвращаем наилучшую сумму, которая была найдена.

---

## Другие решения:

```python
import itertools
def choose_best_sum(t, k, ls):
    try:
        return max(sum(i) for i in itertools.combinations(ls,k) if sum(i)<=t)
    except:
        return None
```

```python
def choose_best_sum(t, k, ls):
    a = len(ls)
    maxdist = None
    possibilities = [bin(x)[2:].zfill(a) for x in range(2 ** a) if bin(x).count('1') == k]
    for i in possibilities:
        dist = sum([int(i[x]) * ls[x] for x in range(len(i))])
        if dist == t:
            return t
        if dist < t:
            maxdist = max(dist, maxdist)
    return maxdist
```
