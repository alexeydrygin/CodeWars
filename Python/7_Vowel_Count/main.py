def count_vowels(string):
    """
    Функция для подсчета количества гласных букв в строке

    Аргументы:
    string -- строка, в которой нужно подсчитать количество гласных букв

    Возвращает:
    Количество гласных букв в строке

    """

    # Создаем множество гласных букв
    vowels = set("aeiou")

    # Инициализируем счетчик гласных букв
    count = 0

    # Проходим по каждой букве в строке
    for char in string:

        # Если буква является гласной, увеличиваем счетчик на 1
        if char in vowels:
            count += 1

    # Возвращаем общее количество гласных букв в строке
    return count
