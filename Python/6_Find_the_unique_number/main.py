def find_uniq(arr):
    # Сравниваем первые три числа
    if arr[0] != arr[1]:
        # Если первые два числа отличаются, проверяем, равно ли третье число одному из них
        if arr[0] == arr[2]:
            return arr[1]
        else:
            return arr[0]
    else:
        # Если первые два числа равны, уникальное число должно быть третьим
        for num in arr:
            if num != arr[0]:
                return num
