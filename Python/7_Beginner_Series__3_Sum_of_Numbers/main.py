# 7 Kyu - Beginner Series #3 Sum of Numbers
def get_sum(a, b):
    # Проверяем, нужно ли поменять местами a и b
    if a > b:
        a, b = b, a
    
    # Считаем сумму, используя формулу для суммы арифметической прогрессии
    return sum(range(a, b+1))
