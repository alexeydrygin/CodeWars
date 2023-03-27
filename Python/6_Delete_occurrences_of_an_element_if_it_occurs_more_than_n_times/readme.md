## 6 kyu - Delete occurrences of an element if it occurs more than n times
[Ссылка на задачу](https://www.codewars.com/kata/554ca54ffa7d91b236000023 "Delete occurrences of an element if it occurs more than n times")

## Enough is enough!

Alice and Bob were on a holiday. Both of them took many pictures of the places they've been, and now they want to show Charlie their entire collection. However, Charlie doesn't like these sessions, since the motif usually repeats. He isn't fond of seeing the Eiffel tower 40 times.  
He tells them that he will only sit for the session if they show the same motif at most `N` times. Luckily, Alice and Bob are able to encode the motif as a number. Can you help them to remove numbers such that their list contains each number only up to `N` times, without changing the order?

## Task

Given a list and a number, create a new list that contains each number of `list` at most `N` times, without reordering.  
For example if the input number is `2`, and the input list is `[1,2,3,1,2,1,2,3]`, you take `[1,2,3,1,2]`, drop the next `[1,2]` since this would lead to `1` and `2` being in the result `3` times, and then take `3`, which leads to `[1,2,3,1,2,3]`.  
With list `[20,37,20,21]` and number `1`, the result would be `[20,37,21]`.  

~~~if:nasm
## NASM notes

Write the output numbers into the `out` parameter, and return its length.

The input array will contain only integers between 1 and 50 inclusive. Use it to your advantage.
~~~

~~~if:c
For C:
* Assign the return array length to the pointer parameter `*szout`.
* Do not mutate the input array.
~~~

~~~if:lambdacalc
## Encodings

purity: `LetRec`  
numEncoding: `Church`  
export constructors `nil, cons` and deconstructor `foldr` for your `List` encoding  
~~~

---
## Задание:

## 6 kyu - Удалить вхождения элемента, если он происходит больше, чем n раз
[Ssshlca na зadaчue] (https://www.codewars.com/kata/554ca54ffa7d91b236000023 "Удалить входы элемента, если он происходит больше, чем n раз")

## Хватит значит хватит!

Алиса и Боб были в отпуске.Они оба сделали много снимков мест, где они были, и теперь они хотят показать Чарли всю свою коллекцию.Тем не менее, Чарли не нравятся эти сеансы, так как мотив обычно повторяется.Он не любит видеть Эйфелевую башню 40 раз.
Он говорит им, что он будет сидеть за сеансом, только если они покажут один и тот же мотив не более максимум.К счастью, Алиса и Боб могут кодировать мотив как число.Можете ли вы помочь им удалить номера, так что их список содержит каждое число только до `n`, без изменения порядка?

## Задача

Учитывая список и номер, создайте новый список, который содержит каждое число `list` больше всего, без переупорядочения.
Например, если входное число равно `2`, а входной список -` [1,2,3,1,2,1,2,3] `, вы принимаете` [1,2,3,1,2]`, Отбросьте следующее` [1,2] `, поскольку это приведет к тому, что` 1` и `2` находится в результате` 3 ', а затем возьмет «3`, что приводит к" [1,2,3, 1,2,3] `.
В списке `[20,37,20,21]` и числа `1`, результат будет` [20,37,21] `.

~~~ if: nasm
## NASM Примечания

Запишите выходные номера в параметр `out` и верните его длину.

Входной массив будет содержать только целые числа от 1 до 50 инклюзивных.Используйте его в своих интересах.
~~~

~~~ if: c
Для C:
* Назначьте длину возврата массива параметру указателя `* szout`.
* Не мутируйте входной массив.
~~~

~~~ if: rambdacalc
## Кодирования

Чистота: `letrec`
numencoding: `church '
Экспортные конструкторы `nil, cons` и деконструктора` foldr` для вашего кодирования `list`
~~~

---

Данный код - функция на языке Python, которая принимает два аргумента: список order и число max_e. Функция возвращает новый список, содержащий каждое число из списка order не более max_e раз, сохраняя исходный порядок элементов.

Первые две строки создают пустой словарь counts и пустой список result.

Затем функция проходит по каждому элементу num в списке order. Если число num не встречалось ранее в списке order, то функция добавляет его в словарь counts со значением 0. Если число num встречалось ранее в списке order менее max_e раз, то функция добавляет его в список result и увеличивает значение counts[num] на 1.

В конце функция возвращает список result.

Например, если вызвать функцию delete_nth([1,2,3,1,2,1,2,3], 2), то она вернет список [1, 2, 3, 1, 2, 3], так как каждое число из списка order содержится в этом списке не более 2 раз. Если вызвать функцию delete_nth([20,37,20,21], 1), то она вернет список [20, 37, 21], так как каждое число из списка order содержится в этом списке не более 1 раза.

## Другие решения:

```python
def delete_nth(order,max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans
```
```python
def delete_nth(order,max_e):
    return [o for i,o in enumerate(order) if order[:i].count(o)<max_e ] # yes!
```
```python
delete_nth = lambda order, max_e: [x for i, x in enumerate(order) if order[:i].count(x) < max_e]
```
