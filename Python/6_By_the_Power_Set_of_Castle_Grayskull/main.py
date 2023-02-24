def power(lst):
    n = len(lst)
    result = []
    # Перебираем все возможные длины подсписков от 0 до n
    for i in range(2**n):
        # Преобразуем i в двоичную строку и дополняем нулями слева
        binary = bin(i)[2:].zfill(n)
        # Используем двоичную строку для выбора элементов из списка
        subset = [lst[j] for j in range(n) if binary[j] == '1']
        result.append(subset)
    return result
