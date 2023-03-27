# 6 kyu - Delete occurrences of an element if it occurs more than n times
def delete_nth(order,max_e):
    counts = {}
    result = []
    for num in order:
        if num not in counts:
            counts[num] = 0
        if counts[num] < max_e:
            result.append(num)
            counts[num] += 1
    return result

"""
Данный код - функция на языке Python, которая принимает два аргумента: список order и число max_e. 

Функция возвращает новый список, содержащий каждое число из списка order не более max_e раз, 

сохраняя исходный порядок элементов.

Первые две строки создают пустой словарь counts и пустой список result.

Затем функция проходит по каждому элементу num в списке order. Если число num не встречалось ранее в списке order, 

то функция добавляет его в словарь counts со значением 0. Если число num встречалось ранее в списке order менее max_e раз, 

то функция добавляет его в список result и увеличивает значение counts[num] на 1.

В конце функция возвращает список result.
"""