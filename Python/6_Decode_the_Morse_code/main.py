from preloaded import MORSE_CODE

def decode_morse(morse_code):
    # Разбиваем входную строку на отдельные слова
    words = morse_code.strip().split('   ')

    # Декодируем каждый символ в каждом слове
    decoded_words = []
    for word in words:
        decoded_word = ''
        for symbol in word.split():
            decoded_word += MORSE_CODE.get(symbol, '')
        decoded_words.append(decoded_word)

    # Соединяем все декодированные слова в строку
    return ' '.join(decoded_words)