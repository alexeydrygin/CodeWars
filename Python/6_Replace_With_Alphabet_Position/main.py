# 6 kyu - Replace With Alphabet Position
def alphabet_position(text):
    # Создаем строку, содержащую все буквы алфавита в нижнем регистре
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    # Создаем пустой список, в который будем добавлять позиции букв
    result = []
    
    # Проходим по каждому символу в строке text в нижнем регистре
    for char in text.lower():
        # Проверяем, является ли символ буквой из алфавита
        if char in alphabet:
            # Если символ является буквой, вычисляем его позицию в алфавите
            # и добавляем позицию в виде строки в список result
            result.append(str(ord(char) - 96))
    
    # Соединяем все элементы списка result в одну строку, разделенную пробелами
    return " ".join(result)