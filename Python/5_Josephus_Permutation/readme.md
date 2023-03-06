## Josephus Permutation

This problem takes its name by arguably the most important event in the life of the ancient historian Josephus: according to his tale, he and his 40 soldiers were trapped in a cave by the Romans during a siege.

Refusing to surrender to the enemy, they instead opted for mass suicide, with a twist: they formed a circle and proceeded to kill one man every three, until one last man was left (and that it was supposed to kill himself to end the act).

Well, Josephus and another man were the last two and, as we now know every detail of the story, you may have correctly guessed that they didn't exactly follow through the original idea.

You are now to create a function that returns a Josephus permutation, taking as parameters the initial array/list of items to be permuted as if they were in a circle and counted out every k places until none remained.

Tips and notes: it helps to start counting from 1 up to n, instead of the usual range 0 to n-1; k will always be >=1.

For example, with an array=[1,2,3,4,5,6,7] and k=3, the function should act this way.

```
[1,2,3,4,5,6,7] - initial sequence
[1,2,4,5,6,7] => 3 is counted out and goes into the result [3]
[1,2,4,5,7] => 6 is counted out and goes into the result [3,6]
[1,4,5,7] => 2 is counted out and goes into the result [3,6,2]
[1,4,5] => 7 is counted out and goes into the result [3,6,2,7]
[1,4] => 5 is counted out and goes into the result [3,6,2,7,5]
[4] => 1 is counted out and goes into the result [3,6,2,7,5,1]
[] => 4 is counted out and goes into the result [3,6,2,7,5,1,4]
```

So our final result is:

```
[3,6,2,7,5,1,4]
```

---

Эта проблема получила свое название в честь, возможно, самого важного события в жизни древнего историка Иосифа Флавия: согласно его рассказу, он и его 40 солдат были заперты римлянами в пещере во время осады.

Отказавшись сдаться врагу, они вместо этого выбрали массовое самоубийство с изюминкой: они образовали круг и продолжали убивать по одному человеку каждые три, пока не остался последний человек (и предполагалось, что он покончит с собой, чтобы закончить акт).

Что ж, Джозефус и еще один человек были последними двумя, и, поскольку мы теперь знаем каждую деталь истории, вы, возможно, правильно догадались, что они не совсем придерживались первоначальной идеи.

Теперь вы должны создать функцию, которая возвращает перестановку Джозефуса, принимая в качестве параметров исходный массив / список элементов, подлежащих перестановке, как если бы они были в круге, и отсчитывая каждые k мест, пока не останется ни одного.

Советы и примечания: это помогает начать отсчет от 1 до n, вместо обычного диапазона от 0 до n-1; k всегда будет > = 1.

Например, с массивом =[1,2,3,4,5,6,7] и k =3 функция должна действовать следующим образом.

```
[1,2,3,4,5,6,7] - initial sequence
[1,2,4,5,6,7] => 3 is counted out and goes into the result [3]
[1,2,4,5,7] => 6 is counted out and goes into the result [3,6]
[1,4,5,7] => 2 is counted out and goes into the result [3,6,2]
[1,4,5] => 7 is counted out and goes into the result [3,6,2,7]
[1,4] => 5 is counted out and goes into the result [3,6,2,7,5]
[4] => 1 is counted out and goes into the result [3,6,2,7,5,1]
[] => 4 is counted out and goes into the result [3,6,2,7,5,1,4]
```

So our final result is:

```
[3,6,2,7,5,1,4]
```

---

Другие решения

```python
def josephus(xs, k):
    i, ys = 0, []
    while len(xs) > 0:
        i = (i + k - 1) % len(xs)
        ys.append(xs.pop(i))
    return ys
```

---

Перестановка Йосифа - это задача на математическую перестановку элементов в круговом порядке. Она получила свое название в честь древнеримского иудейского историка Иосифа Флавия, который описал события, происходившие во время осады Массады.

По легенде, Иосиф и 40 его товарищей были окружены римской армией и приняли решение совершить групповое самоубийство. Они поставились в круг и начали убивать каждого третьего, пока не остался один человек, который должен был совершить самоубийство.

Однако, вместо того чтобы продолжать убивать себя, Иосиф и другой человек решили вместе выжить. Они придумали алгоритм для определения того, какой человек будет убит на каждом шаге, чтобы они оставались последними в живых.

Алгоритм получил название "перестановка Йосифа" и заключается в следующем: участники круга нумеруются от 1 до n, а каждый k-й участник убирается из круга до тех пор, пока не останется только один участник.

Перестановка Йосифа имеет много приложений в информатике, включая использование ее для решения задач связанных с перебором, принятием решений и другими.
