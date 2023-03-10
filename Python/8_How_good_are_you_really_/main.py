# 8 Kyu - How good are you really?

def better_than_average(class_points, your_points):
    # добавляем свой балл в массив баллов класса
    class_points.append(your_points)
    # рассчитываем средний балл класса
    avg = sum(class_points) / len(class_points)
    # сравниваем свой балл со средним баллом класса
    return your_points > avg
