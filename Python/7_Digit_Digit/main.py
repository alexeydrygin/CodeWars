def square_digits(num):
    # преобразуем целое число в строку, чтобы мы могли итерироваться по его цифрам
    digits = str(num)
    result = ""  # инициализируем пустую строку для хранения объединенных цифр
    for digit in digits:  # итерируемся по цифрам и возводим каждую в квадрат, затем объединяем результат
        result += str(int(digit) ** 2)
        # преобразуем объединенные цифры обратно в целое число и возвращаем его
    return int(result)


x = int(input('Введи число:'))
print(square_digits(x))
