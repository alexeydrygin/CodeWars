def is_valid_walk(walk):
    if len(walk) != 10: # если длина прогулки не равна 10, возвращаем False
        return False
    
    x, y = 0, 0 # начальные координаты
    for direction in walk:
        if direction == 'n':
            y += 1
        elif direction == 's':
            y -= 1
        elif direction == 'e':
            x += 1
        elif direction == 'w':
            x -= 1
    
    if x == 0 and y == 0: # если мы вернулись на место, возвращаем True
        return True
    else:
        return False
