def move_zeros(arr):
    zero_count = arr.count(0)   # Подсчитываем количество нулей в массиве
    arr = [elem for elem in arr if elem != 0]  # Удаляем все нули из массива
    arr.extend([0] * zero_count)  # Добавляем нули в конец массива
    return arr
