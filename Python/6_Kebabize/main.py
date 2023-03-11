# 6 Kyu - Kebabize
def kebabize(string):
    # удаляем все цифры из строки
    string = ''.join(c for c in string if not c.isdigit())
    # добавляем '-' перед каждой заглавной буквой, кроме первой
    string = ''.join('-' + c.lower() if c.isupper() and i !=
                     0 else c.lower() for i, c in enumerate(string))
    # удаляем первый символ, если он является '-'
    if string and string[0] == '-':
        string = string[1:]
    return string
