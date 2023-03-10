# 7 Kyu - Friend or Foe?

def friend(x):
    friends = [] # Создаем пустой список для хранения имен друзей
    for y in x: # Итерируемся по списку имен
        if len(y) == 4: # Если имя состоит из 4 букв, добавляем его в список друзей
            friends.append(y)
    return friends # Возвращаем список друзей